import re
from typing import Dict, Any
from parsers.base import BaseParser
from utils.html import HtmlUtils
from utils.date import DateUtils
from environment import TARGET_FORMAT


class TransactionParser(BaseParser):
    """A parser for BAC transactions."""

    def __init__(self):
        self._BAC_TRANSACTION_PATTERN = r'(?:([A-z ]+))(?:\:\$\%|\$\%)(.+?)\$\%'
        self.DATE_SOURCE_FORMAT = '%m%d,%Y,%H:%M'
        self.date_utils = DateUtils()

    def parse(self, html_raw_text: str) -> Dict[str, Any]:
        """
        Parses a BAC transaction from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transaction email.

        Returns:
            A dictionary of the transaction details.
        """
        content = HtmlUtils.extract_content_from_html(
            html_raw_text=html_raw_text, tag_query='td')

        findings = re.findall(self._BAC_TRANSACTION_PATTERN, content,
                              re.DOTALL)

        data = {}

        for item in findings:
            key = item[0]
            value = item[1]
            match key:
                case 'Fecha':
                    data['Fecha'] = self.date_utils.formatter(
                        self.date_utils.replace_month_key_with_number(value),
                        self.DATE_SOURCE_FORMAT, TARGET_FORMAT)
                case 'Monto':
                    data['Moneda'] = value[:3]
                    data['Monto'] = float(value[4:].replace(',', ''))
                case 'VISA' | 'MASTER' | 'AMEX':
                    data['Tarjeta'] = value.replace('*', '')
                case _:
                    data[key] = value
        return data

    def get_mapper_schema(self) -> Dict[str, Any]:
        """
        Returns the schema for the JsonMapperService.
        """
        return {
            'date': 'Fecha',
            'commerce': 'Comercio',
            'currency': 'Moneda',
            'amount': 'Monto',
            'location': 'Ciudad y pais',
            'card': 'Tarjeta',
            'authorization': 'Autorizacion',
            'reference': 'Referencia',
            'transactionType': 'Tipo de Transaccion'
        }
