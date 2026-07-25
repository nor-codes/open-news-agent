import asyncio

from processor.nyt_processor import NewYorkTimesProcessor
from util.config_loader import ConfigLoader
import logging
from datetime import datetime
from models import Config

async def run_job(processor: NewYorkTimesProcessor, config: Config):
    logging.info(f"Running job at {datetime.now()}")
    await processor.process(config)

async def main():
    config = ConfigLoader.load_config()
    processor = NewYorkTimesProcessor(config=config)

    while True:
        try:
            await run_job(processor, config)
        except Exception as e:
            logging.error(e)

        await asyncio.sleep(config.crawler.interval)

if __name__ == "__main__":
    asyncio.run(main())