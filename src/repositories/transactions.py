from typing import Dict, Any
from environment import TEABLE_TRANSACTIONS
from services.teable import TeableService


class TransactionsRepository:
    """Repository for managing transaction records via Teable."""

    def __init__(self) -> None:
        """Initialize the transactions repository with a Teable service instance."""
        self.teable = TeableService()

    def all(self) -> Dict[str, Any]:
        """
        Retrieve a list of transactions from the Teable service.

        Returns:
            A dictionary containing the list of transactions.
        """
        return self.teable.read(TEABLE_TRANSACTIONS)

    def add(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Add a new transaction record.

        Args:
            **kwargs: Transaction fields.

        Returns:
            The created record.
        """
        return self.teable.add(TEABLE_TRANSACTIONS, **kwargs)
