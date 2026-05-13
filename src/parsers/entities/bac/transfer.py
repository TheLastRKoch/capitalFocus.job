import re
from typing import Dict, Any
from parsers.base import BaseParser
from utils.html import HtmlUtils


class TransferParser(BaseParser):
    """A parser for BAC transfers."""

    _BAC_TRANSFER_PATTERN = r'Estimado\(a\)\s([A-z\s]+)\s\:.+?le\scomunica\sque\s([A-z\s]+)\srealizo.+?N°\s([\*\d]+)\.\$.+?dia\s([\d\-]+)\sa\slas\s([\d\:]+).+?por\sun\smonto\sde\s([\d\.\,]+).+?por\sconcepto\sde\:\$\%(.+?)\$\%.+?referencia\ses\s(.+?)\$\%'

    def parse(self, html_raw_text: str) -> Dict[str, Any]:
        """
        Parses a BAC transfer from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transfer email.

        Returns:
            A dictionary of the transfer details, or an empty dictionary
            if no transfer is found.
        """
        result = {}

        content = HtmlUtils.extract_content_from_html(
            html_raw_text=html_raw_text, tag_query='p')
        matches = re.findall(self._BAC_TRANSFER_PATTERN, content, re.DOTALL)

        for match in matches:
            result.update({
                'addressee': match[0],
                'sender': match[1],
                'account': match[2],
                'transactionType': 'TRANSFERENCIA',
                'date': f'{match[3]} {match[4]}',
                'amount': float(match[5].replace('.', '').replace(',', '.')),
                'description': match[6],
                'reference': match[7],
            })
        return result

    def get_mapper_schema(self) -> Dict[str, Any]:
        """
        Returns the schema for the JsonMapperService.
        """
        return {
            'date': 'date',
            'amount': 'amount',
            'reference': 'reference',
            'transactionType': 'transactionType',
        }

    def mapper(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Maps the parsed data and adds custom commerce field.
        """
        mapped_json = super().mapper(data)
        sender = data.get('sender', '')
        addressee = data.get('addressee', '')
        description = data.get('description', '')
        mapped_json['commerce'] = f'{sender} to {addressee} {description}'
        return mapped_json
