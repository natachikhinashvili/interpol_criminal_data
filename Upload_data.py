from google.cloud import bigquery
from google.cloud import storage
import os

def upload_data(dataset_id, table_id, data):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)
    client.insert_rows(table, data)

def upload_images():
    bucket_name = "interpol_criminal_pics"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    for filename in os.listdir('./images'):
        destination_blob_name = f"images/{filename}"
        blob = bucket.blob(destination_blob_name)
        with open(f"./images/{filename}", "rb") as image_file:
            blob.upload_from_file(image_file)

upload_images()