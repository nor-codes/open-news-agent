import yaml
from pathlib import Path
from typing import Dict,Any
import re
import os


def resolve_envs(config):
    config['crawler']["sqs"]["queueArn"] = config['crawler']["sqs"]["queueArn"].replace("${ACCOUNT_ID}", os.getenv("ACCOUNT_ID"))
    return config

class ConfigLoader:

    CONFIG_FILE_PATH = Path("config/config.yaml")
    pattern = re.compile(r"\$\{([^}^{]+)\}")

    @staticmethod
    def load_configuration() -> Dict[str,Any]:
        
        if not ConfigLoader.CONFIG_FILE_PATH.exists():
            raise FileNotFoundError(f"Config file not found: {ConfigLoader.CONFIG_FILE_PATH}")

        with open(ConfigLoader.CONFIG_FILE_PATH, "r") as file:
            config = yaml.safe_load(file)

        return resolve_envs(config)

