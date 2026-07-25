
from typing import List, Dict
from pydantic import BaseModel,Field

class Source(BaseModel):
    name: str = Field(description="Human-readable name of the news source")
    base_url: str = Field(description="Base URL for the source's RSS feeds")
    rss_feed: List[str] = Field(description="List of RSS feed categories/sections to crawl")


class CrawlerConfig(BaseModel):

    interval: int = Field(description="Crawling interval in minutes")
    s3_bucket: str = Field(description="S3 bucket name")
    sqs_queue_arn: str = Field(description="SQS queue arn")
    sources: Dict[str, Source] = Field(description="Mapping of source key (e.g. 'nyt') to source config")
class Config(BaseModel):
    crawler: CrawlerConfig = Field(description="Crawler configuration")

