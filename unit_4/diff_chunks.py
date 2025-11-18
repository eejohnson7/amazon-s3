'''
In this task, we'll perform a multipart upload using different chunk sizes. First, we'll upload a chunk of size 5MB, 
then a chunk of size 6MB, and finally, we'll finish uploading by sending the remaining part of the file. Moreover, we'll not 
use any loop in this task to highlight how we can handle multipart uploads manually. The file we will upload is 
"cosmo-hadoop-course-data-set.zip" and the destination bucket is called "cosmo-archive-2023".

Your task has the following steps:

Initialize the multipart upload.
Upload the first chunk of size 5MB.
Upload the second chunk of size 6MB.
Upload the final chunk, which should contain the rest of the file.
Complete the multipart upload.
'''

import boto3
import os

# Create the S3 client
s3_client = boto3.client('s3')

# Create a new bucket
bucket_name = 'cosmo-archive-2023'
s3_client.create_bucket(Bucket=bucket_name)

# Path to your dataset
file_path = '/usercode/FILESYSTEM/assets/cosmo-hadoop-course-data-set.zip'
key = 'cosmos-hadoop-course-data-set.zip'

# Initiate multipart upload
multipart_upload = s3_client.create_multipart_upload(Bucket=bucket_name, Key=key)
upload_id = multipart_upload['UploadId']

uploaded_parts = []

# Open the file for reading data
with open(file_path, 'rb') as f:
    # Upload the first chunk
    data = f.read(1024 * 1024 * 5)  # 5MB
    response = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=1, UploadId=upload_id, Body=data)
    uploaded_parts.append({'PartNumber': 1, 'ETag': response['ETag']})

    # Upload the second chunk
    data = f.read(1024 * 1024 * 6)  # 6MB
    response = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=2, UploadId=upload_id, Body=data)
    uploaded_parts.append({'PartNumber': 2, 'ETag': response['ETag']})

    # Upload the final chunk (which is the rest of the file)
    data = f.read()
    response = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=3, UploadId=upload_id, Body=data)
    uploaded_parts.append({'PartNumber': 3, 'ETag': response['ETag']})

# Complete the multipart upload
s3_client.complete_multipart_upload(Bucket=bucket_name, Key=key, UploadId=upload_id, MultipartUpload={'Parts': uploaded_parts})
print("Dataset uploaded successfully in chunks of varying sizes. Multipart upload completed.")