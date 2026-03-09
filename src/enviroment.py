from dotenv import load_dotenv
from os import environ as env

load_dotenv()

TEABLE_URL = "https://app.teable.ai"
TEABLE_API_TOKEN = env.get("TEABLE_API_TOKEN")
TEABLE_TRANSACTIONS = env.get("TEABLE_TRANSACTIONS")