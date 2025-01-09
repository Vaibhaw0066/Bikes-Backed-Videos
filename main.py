import time
import requests
import json
import os

API_KEY = "lCbBHJCR2ew5sMCR6ZZm9-mmNb27VtG8X3qFQVcIw9U"


TOKEN_DEV = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNLMmNjOWZ4NnBMRXRXTGxGV3pQVVZrRGFiRDFKIiwidHlwIjoiSldUIn0.eyJhbXIiOlsib2F1dGgiXSwiZHJuIjoiRFMiLCJlbWFpbCI6Imt1bWFyLnZhaWJoYXdAY2FyczI0LmNvbSIsImV4cCI6MTczNjc0ODc1NSwiaWF0IjoxNzM1ODg0NzU1LCJpc3MiOiJQMmNjOWZ2VnBYeWNjZDNxN1ZnSkJNNGdJYmFCIiwibmFtZSI6Ikt1bWFyIFZhaWJoYXciLCJyZXhwIjoiMjAyNS0wMS0zMVQwNjoxMjozNVoiLCJzdWIiOiJVMnE5dFR5UVZiUHNiOGUyWWdVdnhZcEE0UDhNIiwidGVuYW50cyI6eyJlZjc1MzRkZS05MzFlLTRjNjgtOTMyZS02MjZkYTEwOTJmMjkiOnsicGVybWlzc2lvbnMiOltdLCJyb2xlcyI6WyJQVUJMSVNIRVIiXX19fQ.D9kpARpKwOqlBSAzXescLWfIRAFbLGxDPXuI6Accx0MLFwpamxxP0Md5xlcDdxNftu4y8WTX9dheJD7lbAh4cS70THYVX7Eq-Ae1rPm5SzFSnl84iO31dGb6E87OjkdmmstR0XEkiuWp1M-uQudfu1WGYMM3Sx7ayAlRd9KW2DlTE7-LycSTVs2A1XAd1N-Qm8iRFqQwLBgX9xQCO0kEDfmhghQSIwGRXD9zpA2NWQ2Pxp9YAzpwZDssqndLTE_Yt0cwetJ98Z7rKLSLKpEMVSaE8nnYQuG8vU54IBY5hOsHq1qYf5FmXU6_MFomKVVZCkqF6UN2faX8NMDPPjaNsQ"
DEV = "https://cms-bike-backend.qac24svc.dev"


TOKEN_PROD = "eyJhbGciOiJSUzI1NiIsImtpZCI6IlNLMmNzd3RwQTFobFlTSzMyUDU2c1U4b1lGQ1AzIiwidHlwIjoiSldUIn0.eyJhbXIiOlsib2F1dGgiXSwiZHJuIjoiRFMiLCJlbWFpbCI6Im1vaGQuYW1hYW4xQGNhcnMyNC5jb20iLCJleHAiOjE3MzY1NzQ1MjAsImlhdCI6MTczNTcxMDUyMCwiaXNzIjoiUDJjc3d0Zm05Z0lmc0xTWkxKZlI2SXlTNTREeCIsIm5hbWUiOiJNb2hkIEFtYWFuIiwicmV4cCI6IjIwMjUtMDEtMjlUMDU6NDg6NDBaIiwic3ViIjoiVTJkRThoOFdpZ1RreGl4WDdkT1c5aTMzSVZGMSIsInRlbmFudHMiOnsiMTUzMmJmYTEtZTNkOC00MmRiLTg5ODctNWFlNWJiNDc5ZGY4Ijp7InBlcm1pc3Npb25zIjpbXSwicm9sZXMiOlsiUFVCTElTSEVSIl19LCI1ZmEzMjRhYi1mODkzLTRkZDItYjZhZS1kODYwNmQ1N2U2YjUiOnsicGVybWlzc2lvbnMiOltdLCJyb2xlcyI6WyJQVUJMSVNIRVIiXX0sIjZiYTdiODEwLTlkYWQtMTFkMS04MGI0LTAwYzA0ZmQ0MzBjOCI6eyJwZXJtaXNzaW9ucyI6W10sInJvbGVzIjpbIlBVQkxJU0hFUiJdfSwiOGM2NGQ5NjYtN2QwNy00NTJjLTg2NTMtY2IzZWIwNGNhNDVhIjp7InBlcm1pc3Npb25zIjpbXSwicm9sZXMiOlsiUFVCTElTSEVSIl19LCI5YzU1YzZiOC1lZTFjLTRhN2YtYThiNC0zYzQxZDRlNGY2NTciOnsicGVybWlzc2lvbnMiOltdLCJyb2xlcyI6WyJQVUJMSVNIRVIiXX0sImJiZTNiZjU1LTMwYjUtNDU5Zi05M2IxLTNjYzU4NzFkYTkyNiI6eyJwZXJtaXNzaW9ucyI6W10sInJvbGVzIjpbIlBVQkxJU0hFUiJdfSwiZTY0ZWM3YTUtNjc0My00OWVhLTk3ZjMtM2MzN2VkOTAyNWJmIjp7InBlcm1pc3Npb25zIjpbXSwicm9sZXMiOlsiUFVCTElTSEVSIl19LCJlZjc1MzRkZS05MzFlLTRjNjgtOTMyZS02MjZkYTEwOTJmMjkiOnsicGVybWlzc2lvbnMiOltdLCJyb2xlcyI6WyJQVUJMSVNIRVIiXX19fQ.hZvh3jJ_cjL6OP0P39faTfBTPd0xQczJNYuMgEFIlqRlFqw8_4Z7SYxmNzi10HJgVdxom5xCHfpWDRGIGMEOl3hd2i0kG6pv2n82iCGor96SrCIEEubF43l6ZJFqr7G3GAa464h87G3VNKgpUA5Xp53NtJEd77hhxR9MmYEQJ5zvVPksxCB3YLZOK0Z8yqmTw_NVOdz-qQ2GfcyRPgwD2AnSCUoowq_2wLi1YQQlLqRMXGEFMtd2GhLhm0ga7wHZQauSBYs03PiEE65QtYK2iYwvaWYjuJiRL8jnI57vhKI1BtzxLrcb6yACtssNg-MWjTtMGqmaGz8jxhFCJdzj3g"
PROD = "https://cms-bike-backend-prod.cars24.team"

model_video_ids = [101]

# File to store the processed model IDs
response_file = 'response.json'
processed_ids_file = "processed_ids.json"

# Load the processed IDs from the file, if it exists
if os.path.exists(response_file):
    with open(response_file, 'r') as f:
        processed_data = json.load(f)
else:
    processed_data = []

# Function to save the processed IDs to a JSON file
def save_processed_data():
    with open(response_file, 'w') as f:
        json.dump(processed_data, f)

if os.path.exists(processed_ids_file):
    with open(processed_ids_file, 'r') as f:
        processed_ids = json.load(f)
else:
    processed_ids = []

# Function to save the processed IDs to a JSON file
def save_processed_ids():
    with open(processed_ids_file, 'w') as f:
        json.dump(processed_ids, f)

# Function to process a model video ID
def process_video(model_id):
    # Step 2: Fetch model video data from the API
    url = f'{PROD}/api/v1/model-video/{model_id}'
    headers = {
        'sec-ch-ua-platform': 'macOS',
        'Authorization': f'Bearer {TOKEN_PROD}',
        'Referer': 'https://mosaic-dev.24c.in/',
        'tenantId': 'ef7534de-931e-4c68-932e-626da1092f29',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'ngrok-skip-browser-warning': '69420',
        'role': 'PUBLISHER',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()["data"]
        youtube_url = data["url"]
        categories = data['categories']

        # Step 3: Use the YouTube URL to trigger the second API (downloading video)
        download_url = "https://mango.sievedata.com/v2/push"
        download_data = {
            "function": "sieve/youtube_to_mp4",
            "inputs": {
                "url": youtube_url,
                "resolution": "highest-available",
                "include_audio": True
            }
        }

        download_response = requests.post(download_url, json=download_data, headers={
            'Content-Type': 'application/json',
            'X-API-Key': f'{API_KEY}'
        })

        if download_response.status_code == 200:
            download_data = download_response.json()
            job_id = download_data['id']

            # Step 4: Poll the job status until it's finished
            job_status_url = f'https://mango.sievedata.com/v2/jobs/{job_id}'
            for _ in range(100):
                time.sleep(4)
                job_status_response = requests.get(job_status_url, headers={
                    'Content-Type': 'application/json',
                    'X-API-Key': f'{API_KEY}'
                })
                try:
                    if job_status_response.status_code == 200:
                        job_status_data = job_status_response.json()
                        if job_status_data['status'] == 'finished' and job_status_data['outputs'][0]['data']['url']:
                            output_url = job_status_data['outputs'][0]['data']['url']

                            # Step 5: Process the video URL with the final API
                            process_video_url = "http://13.200.213.33:80/process-video"


                            for category in categories:
                                category_id = category["id"]
                                print(f"categorieID :  Model ID {category_id}")
                                # time_data = [{"startTime": category['startTime'], "endTime": category['endTime']}]
                                time_data = [{"startTime": "00:00:01", "endTime": "00:00:10"}]

                                process_data = {
                                    "time": time_data,
                                    "url": output_url,
                                    "modelName": data['model']['name'],
                                    "makeName": data['model']['make']['name'],
                                    "videoName": data['name'],
                                    "mp4Flag": True
                                }

                                process_video_response = requests.post(process_video_url, json=process_data, headers={
                                    'authorization': f'Bearer {TOKEN_PROD}',
                                    'content-type': 'application/json',
                                    'tenantid': 'ef7534de-931e-4c68-932e-626da1092f29',
                                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                                })


                                response_data = dict()
                                response_data["categoriesId"] = category["id"]
                                if process_video_response.status_code == 200:
                                    response_data["videoId"] = process_video_response.json()["data"]["id"]

                                process_data["mp4Flag"] = False
                                process_video_response = requests.post(process_video_url, json=process_data, headers={
                                    'authorization': f'Bearer {TOKEN_PROD}',
                                    'content-type': 'application/json',
                                    'tenantid': 'ef7534de-931e-4c68-932e-626da1092f29',
                                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                                })
                                if process_video_response.status_code == 200:
                                    print(f"Successfully processed video for model ID : {model_id}, categories_id : {category_id}")
                                    # Mark the ID as processed
                                    response_data["gifId"] = process_video_response.json()["data"]["id"]
                                    processed_data.append(response_data)
                                    save_processed_data()

                                    processed_ids.append(model_id)
                                    save_processed_ids()
                                    break

                    else:
                        print(f"Polling failed for job {job_id}")
                        break
                except Exception as e:
                    print(f"Failed to process for model_id {model_id}")
        else:
            print(f"Failed to trigger download for model {model_id}")
    else:
        print(f"Failed to fetch model video for ID {model_id}")

# Step 1: Process each model video ID that hasn't been processed yet
for model_id in model_video_ids:
    if str(model_id) not in processed_ids:
        print(f"Processing for Model ID {model_id}")
        process_video(model_id)
        break
    else:
        print(f"Model ID {model_id} has already been processed.")
