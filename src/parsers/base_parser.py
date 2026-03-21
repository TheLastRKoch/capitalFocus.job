from abc import ABC, abstractmethod


class BaseParser(ABC):
    """Abstract base class for parsers."""

    @abstractmethod
    def parse(self, html_raw_text: str) -> dict:
        """
        Parses an HTML string and returns a dictionary of data.

        Args:
            html_raw_text: The raw HTML string to parse.

        Returns:
            A dictionary of the parsed data.
        """
        pass
