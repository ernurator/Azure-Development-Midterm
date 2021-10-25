import uuid

from azure.storage.blob import BlobServiceClient

import config

blob_service_client = BlobServiceClient.from_connection_string(config.BLOB_STORAGE_CONNECTION_STRING)

CONTAINER_NAME = 'images'


def upload_image(image_content):
    file_name = str(uuid.uuid4()) + ".jpg"
    blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=file_name)
    blob_client.upload_blob(image_content)
    return blob_client.url
