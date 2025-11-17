'''
Space Explorer, a critical observation was made during our code review process concerning the setup of our galactic data 
storage. The script intended to bolster our interstellar exploration data network lacks a crucial detail — it does not specify 
the correct region for the S3 bucket's creation. This oversight could significantly impact data access speeds for our West 
Coast space stations. Your urgent mission is to correct this by configuring the bucket to be explicitly created in the 
'eu-central-1' region. This change is pivotal for enhancing data retrieval performance across our network
'''

import boto3

# Instantiate the S3 resource object
s3_resource = boto3.resource('s3')

# TODO: Create a galactic data bucket in the 'eu-central-1' region instead of the default region
galactic_bucket = s3_resource.create_bucket(
    Bucket='interstellar-galactic-data',
    CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'})
print("Galactic bucket created successfully.")