'''
Prepare to further advance your cloud storage skills with a new challenge: uploading a dataset in smaller increments to 
Amazon S3. Your mission involves dividing a 43 MB dataset into 5 MB chunks and uploading each to the cosmo-archive-2023 
bucket. Utilizing a loop for this multipart upload process, you will demonstrate your ability to efficiently manage large 
datasets in S3. This task is an excellent opportunity to showcase your adeptness in optimizing data transfers and ensuring 
the dataset's accessibility in the cloud.
'''

import boto3
import os

# Initialize the S3 client
s3_client = boto3.client('s3')

# Create a new bucket for your uploads
bucket_name = 'cosmo-archive-2023'
s3_client.create_bucket(Bucket=bucket_name)

# Path to your dataset
file_path = '/usercode/FILESYSTEM/assets/cosmo-hadoop-course-data-set.zip'
key = 'cosmos-hadoop-course-data-set.zip'

# TODO: Initiate a multipart upload session
multipart_upload = s3_client.create_multipart_upload(Bucket=bucket_name, Key=key)
upload_id = multipart_upload['UploadId']

# TODO: Upload the dataset in 5 MB chunks using a loop
part_size = 1024 * 1024 * 5
file_size = os.path.getsize(file_path)
part_count = (file_size + part_size - 1) // part_size
parts = []

with open(file_path, 'rb') as f:
    for part in range(1, part_count + 1):
        data = f.read(part_size)
        response = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=part, UploadId=upload_id, Body=data)
        parts.append({'PartNumber': part, 'ETag': response['ETag']})

# TODO: Complete the multipart upload by combining all the uploaded parts
s3_client.complete_multipart_upload(Bucket=bucket_name, Key=key, UploadId=upload_id, MultipartUpload={'Parts': parts})
print("Dataset uploaded successfully in chunks of varying sizes. Multipart upload completed.")