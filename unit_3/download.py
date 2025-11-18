'''
Hone your AWS S3 capabilities by finalizing a script that interacts with the cloud. A bucket named 
'codesignal-digital-gallery' awaits, intended to house 'prompt-engineering-course-logo.jpg'. Your task is to complete the 
provided script by adding the line necessary for downloading this image into the "usercode/FILESYSTEM/Downloads" directory. 
This step is key to mastering the retrieval and management of cloud-based assets.
'''

import boto3
import os

# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Creating the bucket
bucket_name = 'codesignal-digital-gallery'
s3.create_bucket(Bucket=bucket_name)

# Ensure the Downloads directory exists
os.makedirs('/usercode/FILESYSTEM/Downloads', exist_ok=True)

# Upload a sample image to the bucket first (simulating pre-existing content)
image_file='prompt-engineering-course-logo.jpg'
s3.Bucket(bucket_name).upload_file(f'/usercode/FILESYSTEM/assets/{image_file}', image_file)

# Listing contents of the Downloads folder
print("Downloads folder contents after image download:")
for item in os.listdir('/usercode/FILESYSTEM/Downloads'):
    print(item)

# TODO: Download the 'prompt-engineering-course-logo.jpg' image from the bucket and save it to the '/usercode/FILESYSTEM/Downloads' directory
s3.Bucket(bucket_name) \
    .download_file('prompt-engineering-course-logo.jpg', '/usercode/FILESYSTEM/Downloads/prompt-engineering-course-logo.jpg')

# Listing contents of the Downloads folder
print("Downloads folder contents after image download:")
for item in os.listdir('/usercode/FILESYSTEM/Downloads'):
    print(item)