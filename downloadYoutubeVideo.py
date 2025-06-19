import http.client
import os
import re
import unicodedata
import uuid
from datetime import datetime
import yt_dlp


import boto3
from botocore.exceptions import ClientError, BotoCoreError
from dotenv import load_dotenv
from yt_dlp import DownloadError, YoutubeDL

from logs import getLogger
import logging

load_dotenv()
# ======================= CONFIGURATION =======================
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")
logger = getLogger()


def build_http_response(s3_key, brand, model, cleaned_title, bucket_name,status):
    if(s3_key==None or brand == None):
        result = {
            "status": status,
            "body": None
        }
        return result

    response_data = {
        "fileUrl": s3_key.split("prod/new-car-cms")[1],
        "folderPath": f"{brand}/{model}",
        "brand": brand,
        "model": model,
        "fileName": cleaned_title,
        "s3url": f"https://{bucket_name}/{s3_key}",
        "status": "finished",

    }

    # Simulated HTTP response
    result = {
        "status": status,
        "body": response_data
    }

    return result

def normalize_filename(name):
    """Normalize Unicode and strip unsafe characters."""
    name = unicodedata.normalize("NFKC", name)  # Normalize unicode symbols like ：
    name = name.replace(" ", "-")
    name = re.sub(r"[^a-zA-Z0-9\-_.]", "", name)
    return name

def check_video_exists_on_s3(youtube_url, bucket_name):

    access_key, secret_key, session_token = ACCESS_KEY, SECRET_KEY, SESSION_TOKEN

    try:
        # Step 1: Extract video metadata without downloading
        ydl_opts = {
            'quiet': True,
            'skip_download': True
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            raw_title = info.get('title', 'video')
            normalized_title = unicodedata.normalize("NFKC", raw_title)
            cleaned_title = normalize_filename(normalized_title)

    except DownloadError as e:
        logging.error(f"[YouTube] Video is unavailable or invalid: {e}")
        return None
    except Exception as e:
        logging.error(f"[YouTube] Unexpected error during metadata fetch: {e}")
        return None

    brand = cleaned_title.split("_")[0] if "_" in cleaned_title else "misc"
    model = cleaned_title.split("_")[1] if "_" in cleaned_title else "video"
    year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")
    s3_prefix = f"prod/new-car-cms/{brand}/{model}/{year}/{month}/{day}/"

    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            aws_session_token=session_token if session_token else None,
        )

        response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_prefix)

        if 'Contents' in response:
            for obj in response['Contents']:
                if cleaned_title in obj['Key']:
                    s3_key = obj['Key']
                    s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"

                    return build_http_response(s3_key,brand, model, cleaned_title, bucket_name, 200)
                    # {
                    #     's3_key': s3_key,
                    #     's3_url': s3_url,
                    #     'brand': brand,
                    #     'model': model,
                    #     'title': cleaned_title
                    # }

    except (BotoCoreError, ClientError) as e:
        logging.error(f"[S3] Error accessing S3 bucket: {e}")
        return None
    except Exception as e:
        logging.error(f"[S3] Unexpected error while checking S3: {e}")
        return None

    return None


def downloadAndUploadToS3(youtube_url, download_path, bucket_name):
    logger.log(logging.INFO, "Prod API Hit: Starting video download and upload process")

    os.makedirs(download_path, exist_ok=True)

    ydl_opts = {
        'format': '(bestvideo[height<=1080][height>=720]+bestaudio/best[height<=1080][height>=720])',
        'merge_output_format': 'mp4',
        'outtmpl': f'{download_path}/%(title).200s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }],
        'quiet': False,
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)

            raw_title = info.get('title', 'video')
            normalized_title = unicodedata.normalize("NFKC", raw_title)
            cleaned_title = normalize_filename(normalized_title)

            # Try to find the .mp4 file that contains the normalized title substring
            downloaded_file_path = None
            for file in os.listdir(download_path):
                if file.endswith(".mp4") and normalized_title[:30] in unicodedata.normalize("NFKC", file):
                    downloaded_file_path = os.path.join(download_path, file)
                    break

            if not downloaded_file_path or not os.path.exists(downloaded_file_path):
                raise FileNotFoundError(f"Unable to find merged .mp4 for title: {normalized_title}")

            final_file_path = os.path.join(download_path, f"{cleaned_title}.mp4")

            # Rename only if needed
            if downloaded_file_path != final_file_path:
                os.rename(downloaded_file_path, final_file_path)
                logger.log(logging.INFO, msg=f"Video renamed to: {cleaned_title}.mp4")
            else:
                logger.log(logging.INFO, msg=f"Video already named correctly: {cleaned_title}.mp4")

            logger.log(logging.INFO, msg=f"Video downloaded and renamed: {cleaned_title}.mp4")
    except Exception as e:
        logger.log(logging.ERROR, msg=f"Failed to download video: {youtube_url}, error: {e}")
        result = build_http_response(None, None, None, None, None, 500)
        raise

    brand = cleaned_title.split("_")[0] if "_" in cleaned_title else "misc"
    model = cleaned_title.split("_")[1] if "_" in cleaned_title else "video"

    year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")
    s3_key = f"prod/new-car-cms/{brand}/{model}/{year}/{month}/{day}/{uuid.uuid4()}-{cleaned_title}.mp4"

    try:
        logger.log(logging.INFO,f"Pushing {final_file_path} to s3 bucket")
        s3 = boto3.client(
            "s3",
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN if SESSION_TOKEN else None,
        )

        s3.upload_file(final_file_path, bucket_name, s3_key)
        logger.log(logging.INFO, msg=f"Uploaded to S3: https://{bucket_name}.s3.amazonaws.com/{s3_key}")

    except Exception as e:
        logger.log(logging.ERROR, msg=f"Failed to upload to S3: {e}")
        result = build_http_response(s3_key, brand, model, cleaned_title, bucket_name,400)
        raise
    finally:
        try:
            # os.remove(final_file_path)
            logger.log(logging.INFO, msg=f"Deleted local file: {final_file_path}")
            print()
        except Exception as e:
            logger.log(logging.WARNING, msg=f"Failed to delete local file: {e}")

    result = build_http_response(s3_key,brand,model,cleaned_title,bucket_name, 200)

    logger.log(logging.INFO, msg="Completed upload process.")
    return result


# ======================= TEST RUN =======================
if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=57klwroAddo"
    bucket_name = "cdn.cars24.com"
    download_dir = "downloads"

    try:

        # result = check_video_exists_on_s3(video_url,bucket_name, ACCESS_KEY, SECRET_KEY, SESSION_TOKEN)
        result = downloadAndUploadToS3(video_url, download_dir, bucket_name)
        log_file = f"results-color-videos-{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
        with open(log_file, "w") as f:
            f.write(str(result))
        logger.log(logging.INFO, msg=f"Metadata saved to {log_file}")
    except Exception as e:
        logger.log(logging.ERROR, msg=f"Process failed: {e}")