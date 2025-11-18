'''
Dive into the final task of managing space exploration data using Amazon S3! Your mission is to craft a script that 
activates bucket versioning and sequentially uploads a series of cosmic image files. You are provided with three unique 
images intended for upload in a specific order. Each image will replace the previous one under the same object key, 
"course-logo.jpg", showcasing how versioning in S3 maintains each version of an object, even as it's updated or replaced. 
After uploading all images, retrieve and print all versions of the "course-logo.jpg" to demonstrate the history of changes 
made to this object.
'''

import boto3

s3 = boto3.resource('s3')

# Create a new bucket specifically for our course logos.
bucket_name = 'educational-course-logos'
bucket = s3.create_bucket(Bucket=bucket_name)

# TODO: Enable versioning on this newly created bucket.
s3.BucketVersioning(bucket_name).enable()

# TODO: Upload 'prompt-engineering-course-logo.jpg' from '/usercode/FILESYSTEM/assets/' as 'course-logo.jpg'.
s3_client = boto3.client('s3')
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/prompt-engineering-course-logo.jpg', Bucket=bucket_name, Key='course-logo.jpg')
print("Uploaded prompt-engineering-course-logo.jpg!")

# TODO: Print a confirmation after each upload, ensuring the process is clear.
# TODO: Replace 'course-logo.jpg' by uploading 'machine-learning-course-logo.jpg' from the same directory.
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/machine-learning-course-logo.jpg', Bucket=bucket_name, Key='course-logo.jpg')
print("Uploaded machine-learning-course-logo.jpg!")

# TODO: Finally, upload 'data-science-python-course-logo.jpg', replacing the current 'course-logo.jpg'.
s3_client.upload_file(Filename='/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg', Bucket=bucket_name, Key='course-logo.jpg')
print("Uploaded data-science-python-course-logo.jpg!")

# TODO: Retrieve and print all versions of 'course-logo.jpg', displaying the history of this object.
versions = s3_client.list_object_versions(Bucket=bucket_name, Prefix='course-logo.jpg')
print(versions)