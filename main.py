import os
import uuid

from google.cloud import storage
import urllib.parse as urlparse

import functions_framework

# Triggered by a change in a storage bucket

import config as c
import db
import ai


# GCSクライアントの初期化
storage_client = storage.Client()

# GCSバケット名を設定
BUCKET_NAME = c.BUCKET_NAME

@functions_framework.cloud_event
def gcs_trigger(cloud_event):

    ev = cloud_event

    # イベントデータの取得
    # ファイル情報の取得
    bucket = ev['bucket']
    file_name = ev['name']

    # ファイルの処理
    gs_file_path = f"gs://{bucket}/{file_name}"

    file_path = _get_file_to_local_path(gs_file_path)

    data = ai.generate(file_path)
    os.remove(file_path)

    db.add(data)

    return 'OK', 200

def _get_file_to_local_path(gs_file_path):
    parsed_path = urlparse(gs_file_path)
    if parsed_path.scheme != 'gs':
        raise ValueError("Invalid GCS path. Must start with 'gs://'")

    bucket_name = parsed_path.netloc
    blob_name = parsed_path.path.lstrip('/')

    # GCSクライアントを初期化
    storage_client = storage.Client()

    # バケットとBlobオブジェクトを取得
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # ランダムなUUIDを生成してファイル名とする
    local_filename = str(uuid.uuid4())

    # ファイルの拡張子を保持する場合
    _, file_extension = os.path.splitext(blob_name)
    local_filename += file_extension

    # ファイルをダウンロード
    blob.download_to_filename(local_filename)

    return local_filename
