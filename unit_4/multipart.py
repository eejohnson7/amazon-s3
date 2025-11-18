'''
Embark on a mission to enhance your cloud storage skills by completing a multipart upload to Amazon S3. Your challenge is to 
upload a 43 MB dataset in three parts to the cosmo-archive-2023 bucket. The dataset is segmented into chunks of 15 MB, 15 MB, 
and 13 MB. Although the code for uploading the first chunk is provided, it has not been executed yet. Your objective is to 
finalize the script by seamlessly uploading all three chunks, showcasing your adeptness in managing significant datasets in 
S3 with efficiency and accuracy. This task is your opportunity to demonstrate proficiency in ensuring data integrity and 
accessibility in the cloud.
'''

import boto3

# Configure the S3 client
s3_client = boto3.client('s3')

# Create a new bucket and enable versioning
bucket_name = 'cosmo-archive-2023'
s3_client.create_bucket(Bucket=bucket_name)
s3_client.put_bucket_versioning(Bucket=bucket_name, VersioningConfiguration={'Status': 'Enabled'})

# Path to your large dataset
file_path = '/usercode/FILESYSTEM/assets/cosmo-hadoop-course-data-set.zip'
key = 'cosmos-hadoop-course-data-set.zip'

# Initiate multipart upload
multipart_upload = s3_client.create_multipart_upload(Bucket=bucket_name, Key=key)
upload_id = multipart_upload['UploadId']

# Upload the first chunk (15 MB) as an example
with open(file_path, 'rb') as f:
    data = f.read(1024 * 1024 * 15)  # Read the first 15 MB for the first chunk
    part1 = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=1, UploadId=upload_id, Body=data)

    # TODO: Upload the second chunk of 15 MB
    data = f.read(1024 * 1024 * 15)
    part2 = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=2, UploadId=upload_id, Body=data)
    
    # TODO: Upload the final chunk of 13 MB
    data = f.read()
    part3 = s3_client.upload_part(Bucket=bucket_name, Key=key, PartNumber=3, UploadId=upload_id, Body=data)

# TODO: Complete the multipart upload by combining all the uploaded parts
uploaded_parts = [
    {'PartNumber': 1, 'ETag': part1['ETag']},
    {'PartNumber': 2, 'ETag': part2['ETag']},
    {'PartNumber': 3, 'ETag': part3['ETag']}
]
s3_client.complete_multipart_upload(Bucket=bucket_name, Key=key, UploadId=upload_id, MultipartUpload={'Parts': uploaded_parts})
print("Dataset uploaded successfully in chunks of varying sizes. Multipart upload completed.")