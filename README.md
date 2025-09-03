1. Prerequisites
- Python 3.x
- Google Cloud SDK installed and configured
- A Google Cloud project
- Enabled APIs:
  - Cloud Functions
  - Cloud Scheduler
  - Cloud Storage

2. Create a GCS bucket
3. Deploy the Cloud Function
gcloud functions deploy write_log \
--runtime python310 \
--trigger-http \
--allow-unauthenticated \
--region=us-central1

4. Create a Cloud Scheduler job
gcloud scheduler jobs create http write-log-job \
--schedule "*/1 * * * *" \
--uri "YOUR_CLOUD_FUNCTION_URL" \
--http-method GET


  
