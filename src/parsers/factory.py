from enum import Enum, auto
from parsers.base import BaseParser
from parsers.entities.bac.transaction import TransactionParser
from parsers.entities.bac.transfer import TransferParser
from utils.text import TextUtils


class OperationType(Enum):
    TRANSACTION = auto()
    TRANSFER = auto()


class FactoryParser:
    """A factory for creating parsers."""

    def __init__(self):
        """Initializes the BACParserFactory."""
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
        """
        parser = self._parsers.get(operation_type)
        if not parser:
            raise ValueError(f"No parser found for operation type: {operation_type}")
        return parser

    def get_operation_type(self, text: str) -> OperationType:
        """
        Determines the operation type from the given text.

        Args:
            text: The text to analyze.

        Returns:
            The operation type.
        """
        text = self.text_utils.normalize_text(text)
        if "transferencia" in text:
            return OperationType.TRANSFER
        elif "transaccion" in text:
            return OperationType.TRANSACTION
        return None
