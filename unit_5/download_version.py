'''
We're on a journey with AWS S3 versioning! You are provided with a partially completed Python script that interacts with an 
S3 bucket. The setup work has been done: an S3 bucket named cosmo-course-logos has been created, versioning is enabled for 
the bucket, and two different versions of a logo file have already been uploaded under the same key versioned-course-logo.jpg. 
Your objective is to execute the final steps of the script:

Retrieve All Version IDs: Implement the section of the script that fetches all version IDs for the object named 
versioned-course-logo.jpg. This step is crucial for identifying the available versions of the file.

Download a Specific Version: Based on the version IDs retrieved, modify the script to download the very first version of 
versioned-course-logo.jpg uploaded to the bucket. Note that, due to the reversed chronological order in which they are listed, 
the first version uploaded will be the last in the list. This downloaded file should be saved to the 
/usercode/FILESYSTEM/downloads folder, demonstrating your ability to access and restore specific versions of an object in a 
version-enabled S3 bucket.
'''

import boto3
import os

# Create S3 resource
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

# Ensure that /usercode/FILESYSTEM/downloads folder exists
downloads_folder = "/usercode/FILESYSTEM/downloads"
os.makedirs(downloads_folder, exist_ok=True)

# Create S3 bucket called `cosmo-course-logos`
bucket_name = 'cosmo-course-logos'
s3.create_bucket(Bucket=bucket_name)

# Enable versioning for created bucket
s3.BucketVersioning(bucket_name).enable()

# Upload "/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg" to the bucket under object name "versioned-course-logo.jpg"
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg', Bucket=bucket_name, Key='versioned-course-logo.jpg')

# Upload "/usercode/FILESYSTEM/assets/machine-learning-course-logo.jpg" to the bucket under object name "versioned-course-logo.jpg"
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/machine-learning-course-logo.jpg', Bucket=bucket_name, Key='versioned-course-logo.jpg')

# TODO: Retrieve all version ids for the 'versioned-course-logo.jpg'. Remember, the first version uploaded will be the last in the list due to reverse order.
versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix='versioned-course-logo.jpg')

# TODO: Download the earliest version of 'versioned-course-logo.jpg' to the '/usercode/FILESYSTEM/downloads/' folder
earliest_version = versions['Versions'][-1]['VersionId']
s3_client.download_file(bucket_name, 'versioned-course-logo.jpg', '/usercode/FILESYSTEM/downloads/versioned-course-logo.v' + earliest_version + ".jpg")