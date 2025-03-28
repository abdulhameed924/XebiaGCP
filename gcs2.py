import pandas as pd
import os
import gcsfs  # Library to access Google Cloud Storage

# Set the path to the service account key file directly in the script
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\maham\XebiaGCP\venv\local-bastion-454910-m1-2732b920d5c3.json"

# Define the list of file paths
file_paths = [
    "C:\\Users\\maham\\Downloads\\username-password-recovery-code.csv",
    "C:\\Users\\maham\\Downloads\\username.csv",
    "C:\\Users\\maham\\Downloads\\email.csv"
]

# Define the Google Cloud Storage bucket name
bucket_name = 'bucket8709'

def process_and_upload(file_path, bucket_name):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Convert DataFrame to Parquet format in-memory
    parquet_path = f"gs://{bucket_name}/{os.path.splitext(os.path.basename(file_path))[0]}.parquet"
    
    # Use gcsfs to handle GCS upload
    fs = gcsfs.GCSFileSystem()
    with fs.open(parquet_path, 'wb') as f:
        df.to_parquet(f)

    print(f"File {file_path} processed and uploaded to {parquet_path}")

# Process each file in the list
for file_path in file_paths:
    process_and_upload(file_path, bucket_name)
