import re

from bs4 import BeautifulSoup

from utils.text import TextUtils


class ScraperService:
    """Service for scraping and extracting text patterns from HTML."""

    def __init__(self) -> None:
        """Initialize the scraper service with text utility."""
        self.text_utils = TextUtils()

    def bac_transaction(self, html_raw_text: str) -> dict[str, str]:
        """
        Parse raw HTML text, extract specific paragraph contents, and match them against 
        a predefined regex pattern to build a structured result dictionary.

        Args:
            html_raw_text (str): The raw HTML string to be processed.

        Returns:
            dict[str, str]: A dictionary containing matching keys and their corresponding text values.
        """
        result: dict[str, str] = {}
        content = ""

        html_raw_text = self.text_utils.normalize_text(
            html_raw_text.replace("\n", ""))

        soup = BeautifulSoup(html_raw_text, "html.parser")

        html_text_tags = soup.find_all("p")

        for tag in html_text_tags:
            content += tag.text + "$%"

        pattern = r"(?:([A-z ]+):|(AMEX|VISA|MASTER))\$\%(.+?)\$\%"

        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            key = match[0] if match[0] else match[1]
            value = match[2].strip()

            if key:
                result[key] = value
        return result

    def bac_transfer(self, html_raw_text: str) -> dict[str, str]:
        """
        Parse raw HTML text, extract specific paragraph contents, and match them against
        a predefined regex pattern to build a structured result dictionary.

        Args:
            html_raw_text (str): The raw HTML string to be processed.

        Returns:
            dict[str, str]: A dictionary containing matching keys and their corresponding text values.
        """
        result: dict[str, str] = {}
        content = ""

        html_raw_text = self.text_utils.normalize_text(
            html_raw_text.replace("\n", ""))

        soup = BeautifulSoup(html_raw_text, "html.parser")

        html_text_tags = soup.find_all("p")

        for tag in html_text_tags:
            content += tag.text + "$%"
        return content
        pattern = r"(?:([A-z ]+):|(AMEX|VISA|MASTER))\$\%(.+?)\$\%"

        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            key = match[0] if match[0] else match[1]
            value = match[2].strip()

            if key:
                result[key] = value
        return result
