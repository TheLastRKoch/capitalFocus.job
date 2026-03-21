import re
from enum import Enum, auto

from bs4 import BeautifulSoup

from utils.text import TextUtils


class BACParserService:
    """A service for scraping and extracting text patterns from HTML."""

    _BAC_TRANSACTION_PATTERN = r"(?:([A-z ]+):|(AMEX|VISA|MASTER))\$\%(.+?)\$\%"
    _BAC_TRANSFER_PATTERN = r"Estimado\(a\)\s([A-z\s]+)\s\:.+?le\scomunica\sque\s([A-z\s]+)\srealizo.+?N°\s([\*\d]+)\.\$.+?dia\s([\d\-]+)\sa\slas\s([\d\:]+).+?por\sun\smonto\sde\s([\d\.\,]+).+?por\sconcepto\sde\:\$\%(.+?)\$\%.+?referencia\ses\s(.+?)\$\%"

    transaction_schema = {}
    transfer_schema = {}

    def __init__(self) -> None:
        """Initializes the ScraperService with a text utility."""
        self.text_utils = TextUtils()

    def _extract_content_from_html(self, html_raw_text: str,
                                   tag_query: str) -> str:
        """
        Parses raw HTML and extracts text content from paragraph tags.

        Args:
            html_raw_text: The raw HTML string to process.

        Returns:
            The extracted and concatenated text content.
        """
        normalized_html = self.text_utils.normalize_text(
            html_raw_text.replace("\n", ""))
        soup = BeautifulSoup(normalized_html, "html.parser")
        html_text_tags = soup.find_all(tag_query)
        return "".join(f"{tag.text}$%" for tag in html_text_tags)

    def _create_dict_from_match(self, match: tuple,
                                keys: list[str]) -> dict[str, str]:
        """
        Creates a dictionary from a regex match and a list of keys.

        Args:
            match: The regex match tuple.
            keys: A list of keys for the dictionary.

        Returns:
            The structured dictionary of the details.
        """
        return {keys[i]: match[i] for i in range(len(keys))}

    def get_operation_type(self, text):
        text = self.text_utils.normalize_text(text)
        if "transferencia" in text:
            return self.scrape_transfer
        elif "transaccion" in text:
            return self.scrape_transaction
        return None

    def scrape_transaction(self, html_raw_text: str) -> dict[str, str]:
        """
        Parses a BAC transaction from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transaction email.

        Returns:
            A dictionary of the transaction details.
        """
        content = self._extract_content_from_html(html_raw_text=html_raw_text,
                                                  tag_query="p")
        matches = re.findall(self._BAC_TRANSACTION_PATTERN, content, re.DOTALL)

        return {
            key: match[2].strip()
            for match in matches
            if (key := (match[0] if match[0] else match[1]))
        }

    def scrape_transfer(self, html_raw_text: str) -> dict[str, str]:
        """
        Parses a BAC transfer from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transfer email.

        Returns:
            A dictionary of the transfer details, or an empty dictionary
            if no transfer is found.
        """
        result = {}

        content = self._extract_content_from_html(html_raw_text=html_raw_text,
                                                  tag_query="p")
        matches = re.findall(self._BAC_TRANSFER_PATTERN, content, re.DOTALL)

        for match in matches:
            result.update({
                "addressee": match[0],
                "sender": match[1],
                "account": match[2],
                "date": " ".join([match[3], match[4]]),
                "amount": match[5],
                "description": match[6],
                "reference": match[7],
            })
        return result

    def validate(self, schema, json):
        pass
