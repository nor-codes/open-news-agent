import boto3
import json
import logging
from botocore.exceptions import BotoCoreError, ClientError

class SqsUtil:

    @staticmethod
    def send_message(config, payload):
        try:
            sqs_client = boto3.client('sqs')
            sqs_queue_url = config['crawler']['sqs']['queueArn']  # make sure it's the Queue URL, not ARN
            response = sqs_client.send_message(
                QueueUrl=sqs_queue_url,
                MessageBody=json.dumps(payload)
            )
            logging.info(f"Message sent to SQS: MessageId={response.get('MessageId')}")
        except (BotoCoreError, ClientError) as e:
            logging.error(f"Failed to send message to SQS: {e}")
        except Exception as e:
            logging.error(f"Unexpected error sending message to SQS: {e}")