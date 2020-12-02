#!/usr/bin/env python3
import logging
import boto3
from os import getenv
from botocore.exceptions import ClientError

s3 = boto3.resource(
    service_name='s3',
    region_name=getenv('s3sample_region_name'),
    aws_access_key_id = getenv('aws_access_key'),
    aws_secret_access_key = getenv('aws_secret_key')
)

bucketname=getenv('s3sample_bucketname')

# put your github name here.
your_github_name='xt0fer'
if your_github_name is None:
    raise KeyError("missing a GitHub handle in script")
   
    
def upload_file(resource, file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    s3 = resource
    # Upload the file
    try:
        response = s3.meta.client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


    
your_folder='students/' + your_github_name + '/'
your_filename='kristofer.txt'
objectname = your_folder + your_filename

if upload_file(s3, your_filename, bucketname, objectname) :
    print('upload successful')
else :
    print('upload NOT successful')

with open('downloadfile', 'wb') as f:
    s3.meta.client.download_fileobj(bucketname, objectname, f)
    print('download successful')
