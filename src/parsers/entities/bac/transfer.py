import re
from parsers.base import BaseParser
from utils.html import HtmlUtils


class TransferParser(BaseParser):
    """A parser for BAC transfers."""

    _BAC_TRANSFER_PATTERN = r"Estimado\(a\)\s([A-z\s]+)\s\:.+?le\scomunica\sque\s([A-z\s]+)\srealizo.+?N°\s([\*\d]+)\.\$.+?dia\s([\d\-]+)\sa\slas\s([\d\:]+).+?por\sun\smonto\sde\s([\d\.\,]+).+?por\sconcepto\sde\:\$\%(.+?)\$\%.+?referencia\ses\s(.+?)\$\%"

    def parse(self, html_raw_text: str) -> dict:
        """
        Parses a BAC transfer from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transfer email.

        Returns:
            A dictionary of the transfer details, or an empty dictionary
            if no transfer is found.
        """
        result = {}

        content = HtmlUtils.extract_content_from_html(html_raw_text=html_raw_text,
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
