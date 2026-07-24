from typing import Dict, Any, List
from services.service_client import ServiceClient


class TransactionsRepository:
    """Repository for managing transaction records via capitalFocus.service API."""

    def __init__(self) -> None:
        """Initialize the transactions repository with a service client instance."""
        self.service_client = ServiceClient()

    def submit(self, transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Submit transactions to capitalFocus.service.

        Args:
            transactions: A list of transaction dictionaries to submit.

        Returns:
            A dictionary containing the status and number of created records.
        """
        return self.service_client.submit_transactions(transactions)
