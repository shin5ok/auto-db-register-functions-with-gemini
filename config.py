
import os
e = os.environ

PROJECT = e.get("PROJECT_ID")
REGION = e.get("REGION", "us-central1")
BUCKET_NAME = e.get("BUCKET_NAME")

COLLECTION_NAME = e.get("COLLECTION_NAME", "data")

GEN_CONFIG = generation_config = {
    "max_output_tokens": 8192,
    "temperature": 0,
    "top_p": 1,
    "response_mime_type": "application/json",
}
