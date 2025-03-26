from google.cloud import storage

# Create a GCS client
client = storage.Client()

def create_bucket(bucket_name):
    """Creates a new bucket in specified location with given name."""
    try:
        new_bucket = client.create_bucket(bucket_name)
        print(f"Bucket {new_bucket.name} created.")
    except Exception as e:
        print(f"Failed to create bucket: {e}")

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the specified bucket."""
    try:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        print(f"Failed to upload blob: {e}")

def list_blobs(bucket_name, prefix):
    """Lists all the blobs in the bucket that begin with the prefix."""
    try:
        bucket = client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=prefix)

        for blob in blobs:
            print(blob.name)
    except Exception as e:
        print(f"Failed to list blobs: {e}")

# Create bucket
create_bucket('buck8701')

# Upload file
upload_blob('buck8701', 'C:\\Users\\maham\\OneDrive\\Documents\\MS Data Science\\1st Semester\\CIS 322 DSFA\\Week 3\\Mohammed_Week4.docx', 'first/Mohammed_Week4.docx')

# List all files in the 'first/' directory
list_blobs('buck8701', 'first/')
