'''
Dive into AWS S3 with Boto3 by adding a new picture to a digital gallery. Your job is to finish up a script that sets up a 
bucket named codesignal-digital-gallery and then uploads a specific image file into it. To get started, add the missing code 
to upload the image. After running the script with the Run button, you'll see the bucket being created, the image getting 
uploaded, and a before-and-after list showing what's in the bucket. This proves your image is now part of the gallery.
'''

import boto3

# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Creating the bucket
bucket_name = 'codesignal-digital-gallery'
s3.create_bucket(Bucket=bucket_name)

# Pre-upload bucket contents listing
print("Bucket contents before upload:")
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)

# TODO: Upload the '/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg' image to the bucket
s3.Bucket('codesignal-digital-gallery') \
.upload_file('/usercode/FILESYSTEM/assets/data-science-python-course-logo.jpg', 'data-science-python-course-logo.jpg')

# Post-upload bucket contents listing
print("\nBucket contents after upload:")
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)