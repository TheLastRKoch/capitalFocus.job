from os import environ as env
from dotenv import load_dotenv
import logging

load_dotenv()

TEABLE_URL = 'https://app.teable.ai'
TEABLE_API_TOKEN = env.get('TEABLE_API_TOKEN')
TEABLE_TRANSACTIONS = env.get('TEABLE_TRANSACTIONS')

TARGET_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    filename=env.get('LOG_PATH'),
    filemode='a',
    level=logging.INFO if env.get('LOG_LEVEL') == 'info' else logging.DEBUG,
    format=env.get('LOG_FORMAT')
)
