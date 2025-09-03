from datetime import datetime
from google.cloud import storage
from zoneinfo import ZoneInfo

def write_log(event=None, context=None):
    now = datetime.now(ZoneInfo("Asia/Ho_Chi_Minh")).strftime("%Y-%m-%d %H:%M:%S")
    message = f"Hi guys! [{now}]"

    storage_client = storage.Client()
    bucket_name = "bucket-scheduler-demo"
    file_name = "log.txt"

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)

    old_data = ""
    if blob.exists():
        old_data = blob.download_as_text()

    new_data = old_data + message + "\n"
    blob.upload_from_string(new_data)

    print(f"Appended log: {message}")

    return {"status": "success", "message": message}
