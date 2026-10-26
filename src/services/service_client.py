import requests
from typing import Dict, Any, List
from environment import SERVICE_URL
import logging

logger = logging.getLogger(__name__)


class ServiceClient:
    """HTTP client for communicating with capitalFocus.service API."""

    def __init__(self) -> None:
        """Initialize the service client."""
        self.base_url = f'{SERVICE_URL}/api/transactions'
        self.headers = {'Content-Type': 'application/json'}

    def submit_transactions(self, transactions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Submit validated transactions to capitalFocus.service.

        Args:
            transactions: A list of transaction dictionaries to submit.

        Returns:
            The JSON response from the service containing status and created count.

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
            ValueError: If the response is invalid.
        """
        if not isinstance(transactions, list):
            raise ValueError('Transactions must be a list')

        if not transactions:
            logger.warning('No transactions to submit')
            return {'status': 'success', 'created': 0}

        url = f'{self.base_url}/'
        try:
            logger.info(f'Submitting {len(transactions)} transaction(s) to {url}')
            response = requests.post(
                url,
                json=transactions,
                headers=self.headers,
                timeout=30
            )
            response.raise_for_status()
            result = response.json()
            logger.info(f'Successfully created {result.get("created", 0)} transaction(s)')
            return result
        except requests.exceptions.ConnectionError as e:
            logger.error(f'Connection error to service: {str(e)}')
            raise
        except requests.exceptions.Timeout as e:
            logger.error(f'Request timeout to service: {str(e)}')
            raise
        except requests.exceptions.HTTPError as e:
            logger.error(f'HTTP error from service: {e.response.status_code} - {e.response.text}')
            raise
        except Exception as e:
            logger.error(f'Unexpected error submitting transactions: {str(e)}')
            raise
