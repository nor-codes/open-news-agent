import logging

import boto3
from botocore.exceptions import ClientError


class S3Util:

    def __init__(self, client):
        self.client = client

    @staticmethod
    def put_object(bucket, key, content):
        try:
            client = boto3.client('s3')
            client.put_object(Bucket=bucket, Key=key, Body=content)
            logging.info(f"S3 put successful - {key}")
        except ClientError as e:
            err_code = e.response['Error']['Code']
            logging.error(f"S3 put failed - {err_code}")