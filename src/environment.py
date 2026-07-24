from os import environ as env
from dotenv import load_dotenv
import logging

load_dotenv()

SERVICE_URL = env.get('SERVICE_URL', 'http://localhost:8000')

TARGET_FORMAT = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    filename=env.get('LOG_PATH'),
    filemode='a',
    level=logging.INFO if env.get('LOG_LEVEL') == 'info' else logging.DEBUG,
    format=env.get('LOG_FORMAT')
)
