'''
Greetings, Space Voyager! As you have successfully enabled versioning on a bucket in the previous task, it's now time to 
suspend versioning for a bucket. Being able to suspend versioning is crucial for managing costs, as versioning stores all 
versions of an object, including all writes and deletes. Let's put your skills to the test, shall we?
'''

import boto3

# Initialize S3 resource
s3_resource = boto3.resource('s3')

bucket_name = 'cosmo-archive-bucket-2023'
s3_resource.create_bucket(Bucket=bucket_name)
s3_resource.BucketVersioning(bucket_name).enable()

# TO DO: Suspend the versioning
s3_resource.BucketVersioning(bucket_name).suspend()
# TO DO: Print the bucket versioning status
print(s3_resource.BucketVersioning(bucket_name).status)