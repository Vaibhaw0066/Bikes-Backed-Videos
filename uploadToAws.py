import os
import uuid
import boto3
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")

# Function to upload files to S3 bucket
def upload_files_to_s3(local_path, bucket_name):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )

    uploaded_files = []
    i = 0

    # Walk through the local folder structure
    for root, dirs, files in os.walk(local_path):
        for file_name in files:
            if ".DS_Store" == file_name:
                continue
            if "desktop.ini" == file_name:
                continue

            file_path = os.path.join(root, file_name)

            # Extract brand and model from local folder structure
            brand = file_name.split("_")[0]
            model = file_name.split("_")[1]
            print(file_name, brand, model)

            # # Generate S3 key
            year, month, day = datetime.now().strftime("%Y-%m-%d").split("-")
            s3_key = f"prod/new-car-cms/{brand}/{model}/{year}/{month}/{day}/{str(uuid.uuid4())}-{file_name}".replace(
                " ", "-"
            )

            # # Upload file to S3 bucket
            s3.upload_file(file_path, bucket_name, s3_key)

            # # Construct file URL
            file_url = f"s3://{bucket_name}/{s3_key}"
            folder_path = f"{brand}/{model}"

            # Append uploaded file details to the list
            uploaded_files.append(
                {
                    "fileUrl": s3_key.split("prod/new-car-cms")[1],
                    "folderPath": folder_path,
                    "brand": brand,
                    "model": model,
                    "fileName": file_name.split(".")[0].replace(" ", "-"),
                    "s3url": file_url,
                }
            )
            i += 1
            # if i == 10:
            #     break

    return uploaded_files


# Example usage
if __name__ == "__main__":
    local_folder_path = "4 April"
    bucket_name = "cdn.cars24.com"

    uploaded_files = upload_files_to_s3(local_folder_path, bucket_name)

    with open(f"results-color-images-{datetime.now()}.txt", "w") as f:
        # with open(f"results-color-images.txt", "w") as f:
        f.write(str(uploaded_files))
    # print(uploaded_files)