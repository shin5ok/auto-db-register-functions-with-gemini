import os
e = os.environ
PROJECT = e.get("PROJECT_ID")
REGION = e.get("REGION", "us-central1")
BUCKET_NAME = e.get("BUCKET_NAME")

GEN_CONFIG = generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0,
    "top_p": 0.95,
    "response_mime_type": "application/json",
}
