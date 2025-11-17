'''
Great job making it this far, Space Explorer! You've learned a lot about managing S3 buckets with Boto3. For your final 
mission, let's apply all that knowledge. You're tasked with creating two S3 buckets: 'intergalactic-archive-us' in the 
default us-east-1 region and 'intergalactic-archive-eu' in the eu-central-1 region. Then, list all your buckets to see your 
entire galactic collection. Conclude your mission by safely removing the 'intergalactic-archive-eu' bucket.
'''

import boto3

# TODO: Initialize the S3 resource variable using boto3
s3_resource = boto3.resource('s3')

# TODO: Create a bucket named 'intergalactic-archive-us' in the default region
us_bucket = s3_resource.create_bucket(Bucket='intergalactic-archive-us')

# TODO: Create another bucket named 'intergalactic-archive-eu' in the eu-central-1 region
eu_bucket = s3_resource.create_bucket(
    Bucket='intergalactic-archive-eu',
    CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'}
)

# TODO: Print all bucket names available in your AWS account after the creation
buckets = s3_resource.buckets.all()
for bucket in buckets:
    print(bucket.name)

# TODO: Delete the 'intergalactic-archive-eu' bucket.
s3_resource.Bucket('intergalactic-archive-eu').delete()

# TODO: Print all remaining buckets after the deletion
buckets = s3_resource.buckets.all()
for bucket in buckets:
    print(bucket.name)