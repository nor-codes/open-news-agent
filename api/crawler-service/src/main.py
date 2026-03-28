from processor.nyt_processor import NewYorkTimesProcessor
from util.config_loader import ConfigLoader
from dotenv import load_dotenv
import time
import os
from datetime import datetime

load_dotenv()
config = ConfigLoader.load_configuration()

INTERVAL = int(os.getenv("CRAWLER_INTERVAL", 3600))  # seconds

processor = NewYorkTimesProcessor()

while True:
    try:
        print(f"Running job at {datetime.now()}")
        processor.process(config)
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(INTERVAL)