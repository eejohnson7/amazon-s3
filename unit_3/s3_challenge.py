'''
Embark on the ultimate Boto3 and AWS S3 challenge, encapsulating the entire lifecycle of S3 bucket management. 
From creation to clean-up, this task will test your proficiency in handling cloud storage with precision. You'll start by 
creating a new bucket, then populate it with a series of images that represent various courses from CodeSignal Learn. 
After verifying the uploaded contents, you'll remove all objects and finally delete the bucket itself, showcasing a full 
spectrum of S3 management skills. Prepare to execute each step and observe the transformative journey of your S3 bucket from 
inception to conclusion.
'''

import boto3

# Initialize the boto3 S3 resource
s3 = boto3.resource('s3')

# Create a new bucket
bucket_name = 'full-cycle-management-challenge'

# TODO: Create the bucket using the bucket_name variable
s3.create_bucket(Bucket=bucket_name)

# Names of the images to be uploaded
images = [
    'prompt-engineering-course-logo.jpg',
    'machine-learning-course-logo.jpg',
    'data-science-python-course-logo.jpg'
]

# TODO: Upload the images to the bucket from '/usercode/FILESYSTEM/assets/'
for img in images:
    s3.Bucket(bucket_name).upload_file('/usercode/FILESYSTEM/assets/' + img, img)

# TODO: List the contents of the bucket
for obj in s3.Bucket(bucket_name).objects.all():
    print(obj.key)

# TODO: Delete all objects from the bucket
s3.Bucket(bucket_name).objects.all().delete()

# TODO: Delete the bucket itself
s3.Bucket(bucket_name).delete()