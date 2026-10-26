from enum import Enum, auto
from typing import Optional
from parsers.base import BaseParser
from parsers.entities.bac.transaction import TransactionParser
from parsers.entities.bac.transfer import TransferParser
from utils.text import TextUtils


class OperationType(Enum):
    """Enumeration of supported operation types."""
    TRANSACTION = auto()
    TRANSFER = auto()


class FactoryParser:
    """A factory for creating parsers."""

    def __init__(self) -> None:
        """Initializes the FactoryParser."""
        self._parsers = {
            OperationType.TRANSACTION: TransactionParser(),
            OperationType.TRANSFER: TransferParser(),
        }
        self.text_utils = TextUtils()

    def get_parser(self, operation_type: OperationType) -> BaseParser:
        """
        Gets the parser for the given operation type.

        Args:
            operation_type: The type of operation.

        Returns:
            The parser for the given operation type.

        Raises:
            ValueError: If no parser is found for the operation type.
        """
        parser = self._parsers.get(operation_type)
        if not parser:
            raise ValueError(
                f'No parser found for operation type: {operation_type}')
        return parser

    def get_operation_type(self, text: str) -> Optional[OperationType]:
        """
        Determines the operation type from the given text.

        Args:
            text: The text to analyze.

        Returns:
            The operation type, or None if undetermined.
        """
        normalized_text = self.text_utils.normalize_text(text).lower()
        if 'transferencia' in normalized_text:
            return OperationType.TRANSFER
        if 'transaccion' in normalized_text:
            return OperationType.TRANSACTION
        return None
