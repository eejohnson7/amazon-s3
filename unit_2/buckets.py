'''
Embark on a journey through AWS S3, where you're tasked with organizing your cosmic voyage memories and data across the 
galaxy. In this scenario, you will create three S3 buckets located in different regions to store photos from your 
intergalactic travels in 2024, widget data, and document archives from 2020. Witness firsthand how to manage these buckets 
within AWS: you'll see the listing of all your created buckets, perform a deletion operation on one, and then observe the 
updated list of buckets.

Simply click Run to see these S3 operations in action, showcasing the ease and power of managing cloud storage with AWS. No 
coding is required on your part for this task; enjoy watching your galactic storage system come to life!
'''

import boto3

s3_resource = boto3.resource('s3')

s3_resource.create_bucket(Bucket='cosmo-galaxy-photos-2024') # Creating bucket in the default us-east-1 region
s3_resource.create_bucket(Bucket='cosmo-widget-data', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})  # Creating bucket in the us-west-2 region
s3_resource.create_bucket(Bucket='cosmo-doc-archive-2020', CreateBucketConfiguration={'LocationConstraint': 'eu-central-1'})  # Creating bucket in the eu-central-1 region

print("Buckets before deletion:")
for bucket in s3_resource.buckets.all():
    print(bucket.name)

s3_resource.Bucket('cosmo-doc-archive-2020').delete()

print("\nBuckets after deletion:")
for bucket in s3_resource.buckets.all():
    print(bucket.name)
    
"""
Expected output:

Buckets before deletion:
cosmo-galaxy-photos-2024
cosmo-widget-data
cosmo-doc-archive-2020

Buckets after deletion:
cosmo-galaxy-photos-2024
cosmo-widget-data
"""