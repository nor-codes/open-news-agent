import requests
import logging
from datetime import date, datetime
from util.s3_util import S3Util
import uuid

from util.sqs_util import SqsUtil


class NewYorkTimesProcessor:

    def process(self, config):
        source = config["crawler"]["sources"]["nyt"]
        now = datetime.now()

        # Bucket folder by date (YYYY_MM_DD)
        bucket = f"{config['crawler']['s3']['bucket']}/{now.strftime('%Y_%m_%d')}"

        base_url = source['baseUrl']

        for feed in source['rssFeed']:
            url = f"{base_url}/{feed}.xml"
            logging.info(f"Fetch -> New York Times Feed - {url}")

            try:
                response = requests.get(url)
                response.raise_for_status()  # will raise HTTPError if not 200

                # Timestamp for object key
                timestamp = now.strftime("%Y%m%d_%H%M%S")
                object_key = f"{feed}_{timestamp}.xml"

                content = response.content.decode('utf-8')

                message_body = {
                    "id": str(uuid.uuid4()),
                    "time-stamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "object-id": object_key,
                    "s3-bucket": bucket
                }

                # Send to SQS safely
                SqsUtil.send_message(config, message_body)

                # Upload to S3 safely
                S3Util.put_object(bucket, object_key, content)

            except requests.HTTPError as e:
                logging.error(f"HTTP error fetching feed {url}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error processing feed {url}: {e}")