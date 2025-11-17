'''
Moving on to AWS services, in this task, you will demonstrate the creation of custom and default AWS sessions using Boto3, 
an important aspect of working with AWS in Python. Amazon S3 is the service with which you are going to interact in this task. 
Your job is to complete the given script by creating a default S3 resource and client, which will connect to AWS services using 
the default session. The default session contains credentials and settings from environmental variables, AWS credentials and 
config files, or IAM roles for Amazon EC2 instances.
'''

import boto3

# Create an AWS session with explicit credentials and region
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
    region_name='us-west-2'
)

# Create an S3 resource based on the session
s3_resource = session.resource('s3')

# Create an S3 client based on the session
s3_client = session.client('s3')

# TODO: Create a default S3 resource with the default session
default_s3_resource = boto3.resource('s3')

# TODO: Create a default S3 client with the default session
default_s3_client = boto3.client('s3')