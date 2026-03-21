import re
from parsers.base import BaseParser
from utils.html import HtmlUtils


class TransactionParser(BaseParser):
    """A parser for BAC transactions."""

    _BAC_TRANSACTION_PATTERN = r"(?:([A-z ]+):|(AMEX|VISA|MASTER))\$\%(.+?)\$\%"

    def parse(self, html_raw_text: str) -> dict:
        """
        Parses a BAC transaction from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transaction email.

        Returns:
            A dictionary of the transaction details.
        """
        content = HtmlUtils.extract_content_from_html(html_raw_text=html_raw_text,
                                                      tag_query="p")
        matches = re.findall(self._BAC_TRANSACTION_PATTERN, content, re.DOTALL)

        return {
            key: match[2].strip()
            for match in matches
            if (key := (match[0] if match[0] else match[1]))
        }
