import re
from typing import Dict, Any
from parsers.base import BaseParser
from utils.html import HtmlUtils


class TransactionParser(BaseParser):
    """A parser for BAC transactions."""

    _BAC_TRANSACTION_PATTERN = r'(?:([A-z ]+))(?:\:\$\%|\$\%)(.+?)\$\%'

    def parse(self, html_raw_text: str) -> Dict[str, Any]:
        """
        Parses a BAC transaction from an HTML string.

        Args:
            html_raw_text: The raw HTML string of the transaction email.

        Returns:
            A dictionary of the transaction details.
        """
        content = HtmlUtils.extract_content_from_html(
            html_raw_text=html_raw_text, tag_query='p')

        findings = re.findall(self._BAC_TRANSACTION_PATTERN, content,
                              re.DOTALL)

        data = {}

        for item in findings:
            key = item[0]
            value = item[1]
            match key:
                case 'VISA' | 'MASTER' | 'AMEX':
                    data['Tarjeta'] = value.replace('*', '')
                case 'Monto':
                    data['Moneda'] = value[:3]
                    data['Monto'] = float(value[4:].replace(',', ''))
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
