import re
from parsers.base import BaseParser
from utils.html import HtmlUtils


class TransactionParser(BaseParser):
    """A parser for BAC transactions."""

    _BAC_TRANSACTION_PATTERN = r"(?:([A-z ]+))(?:\:\$\%|\$\%)(.+?)\$\%"

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

        findings = re.findall(self._BAC_TRANSACTION_PATTERN, content, re.DOTALL)

        data = {}

        for item in findings:
            match item[0]:
                case 'VISA' | 'MASTER' | 'AMEX':
                    data["Tarjeta"] = item[1]
                case _:
                    data[item[0]] = item[1]
        return data
