from os import environ as env
from dotenv import load_dotenv

load_dotenv()

TEABLE_URL = 'https://app.teable.ai'
TEABLE_API_TOKEN = env.get('TEABLE_API_TOKEN')
TEABLE_TRANSACTIONS = env.get('TEABLE_TRANSACTIONS')

TARGET_FORMAT = "%Y-%m-%d %H:%M:%S"
