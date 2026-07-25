import yaml
from pathlib import Path
from typing import Dict,Any
from models import Config
import re
import os


def resolve_envs(config):
    config['crawler']["sqs"]["queueArn"] = config['crawler']["sqs"]["queueArn"].replace("${ACCOUNT_ID}", os.getenv("ACCOUNT_ID"))
    return config

class ConfigLoader:

    CONFIG_FILE_PATH = Path("config.yaml")
    pattern = re.compile(r"\$\{([^}^{]+)\}")

    @staticmethod
    def load_config() -> Config:
        
        if not ConfigLoader.CONFIG_FILE_PATH.exists():
            raise FileNotFoundError(f"Config file not found: {ConfigLoader.CONFIG_FILE_PATH}")

        with open(ConfigLoader.CONFIG_FILE_PATH) as file:
            raw_config = file.read()

        resolved_config = os.path.expandvars(raw_config)
        yaml_config = yaml.safe_load(resolved_config)

        return Config(**yaml_config)

