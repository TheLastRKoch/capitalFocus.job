import requests
from typing import Dict, Any
from environment import TEABLE_API_TOKEN, TEABLE_URL


class TeableService:
    """Service for interacting with the Teable API."""

    def __init__(self) -> None:
        """Initialize the Teable service."""
        self.base_url = f'{TEABLE_URL}/api/table'

    def __get_headers(self) -> Dict[str, str]:
        """
        Generate HTTP headers for Teable API requests.

        Returns:
            A dictionary containing the authorization bearer token.
        """
        return {'Authorization': f'Bearer {TEABLE_API_TOKEN}'}

    def read(self, table_id: str) -> Dict[str, Any]:
        """
        Retrieve records from a specified table.

        Args:
            table_id: The ID of the table to read.

        Returns:
            The JSON response from the Teable API.
        """
        url = f'{self.base_url}/{table_id}/record'
        response = requests.get(url, headers=self.__get_headers(), timeout=10)
        response.raise_for_status()
        return response.json()

    def add(self, table_id: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Add a new record to a specified table.

        Args:
            table_id: The ID of the table to add to.
            **kwargs: The fields to add to the record.

        Returns:
            The JSON response from the Teable API.
        """
        url = f'{self.base_url}/{table_id}/record'
        data = {
            'fieldKeyType': 'name',
            'records': [
                {
                    'fields': kwargs
                }
            ]
        }
        response = requests.post(
            url,
            headers=self.__get_headers(),
            json=data,
            timeout=10
        )
        response.raise_for_status()
        return response.json()
