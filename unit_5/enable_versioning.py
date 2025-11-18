'''
Excellent work, Space Explorer! Now, it's time to solidify your understanding of S3 versioning. Your space mission depends 
on mastering data version control for efficient archiving in the cloud. Can you enable versioning on a bucket? This is a 
crucial step to ensure that every version of your data is secured and retrievable.
'''

import boto3

# Initialize S3 resource
s3_resource = boto3.resource('s3')

bucket_name = 'archive-bucket'
# TODO: Create a new bucket and enable the versioning for it
s3_resource.create_bucket(Bucket=bucket_name)
bucket_versioning = s3_resource.BucketVersioning(bucket_name)
bucket_versioning.enable()