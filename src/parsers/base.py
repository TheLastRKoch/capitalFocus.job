from abc import ABC, abstractmethod
from typing import Dict, Any
from services.json_mapper import JsonMapperService


class BaseParser(ABC):
    """Abstract base class for parsers."""

    @abstractmethod
    def parse(self, html_raw_text: str) -> Dict[str, Any]:
        """
        Parses an HTML string and returns a dictionary of data.

        Args:
            html_raw_text: The raw HTML string to parse.

        Returns:
            A dictionary of the parsed data.
        """

    @abstractmethod
    def get_mapper_schema(self) -> Dict[str, Any]:
        """
        Returns the schema for the JsonMapperService.

        Returns:
            A dictionary representing the mapping schema.
        """

    def mapper(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Maps the parsed data to a unified format.

        Args:
            data: The parsed data dictionary.

        Returns:
            A mapped dictionary.
        """
        schema = self.get_mapper_schema()
        mapper_service = JsonMapperService(schema)
        return mapper_service.transform(data)
