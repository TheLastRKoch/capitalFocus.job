from enviroment import TEABLE_TRANSACTIONS
from services.teable import TeableService


class TransactionsRepository:

    def __init__(self):
        self.teable = TeableService()

    def get_list(self):
        return self.teable.read(TEABLE_TRANSACTIONS)
