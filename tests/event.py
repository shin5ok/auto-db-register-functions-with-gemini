import requests
import json
from datetime import datetime

def send_test_event(url, bucket_name, file_name):
    headers = {
        "Content-Type": "application/json",
        "Ce-Id": "1234567890",
        "Ce-Specversion": "1.0",
        "Ce-Type": "google.cloud.storage.object.v1.finalized",
        "Ce-Time": datetime.utcnow().isoformat() + "Z",
        "Ce-Source": f"//storage.googleapis.com/projects/_/buckets/{bucket_name}"
    }

    payload = {
        "bucket": bucket_name,
        "name": file_name,
        "metageneration": "1",
        "timeCreated": datetime.utcnow().isoformat() + "Z",
        "updated": datetime.utcnow().isoformat() + "Z"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

if __name__ == "__main__":
    url = "http://localhost:8080"  # あなたのローカルサーバーのURL
    bucket_name = "your-bucket-name"
    file_name = "path/to/your/file.txt"
    
    send_test_event(url, bucket_name, file_name)
