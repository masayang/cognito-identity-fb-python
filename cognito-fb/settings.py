from os.path import join, dirname
from dotenv import load_dotenv
import os
import json


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


config = {
    "KEY": os.environ.get("KEY"),
    "AWS": {
        "ACCOUNT_ID": os.environ.get("AWS_ACCOUNT_ID"),
        "IDENTITY_POOL_ID": os.environ.get("AWS_IDENTITY_POOL_ID"),
        "REGION": os.environ.get("AWS_REGION")
    },
    "API": {
        "BASE_ARN": os.environ.get("API_BASE_ARN")
    }
}


if __name__ == '__main__':
    print(json.dumps(config, indent=4, sort_keys=True))