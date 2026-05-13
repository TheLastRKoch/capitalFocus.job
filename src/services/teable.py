import requests
from environment import TEABLE_API_TOKEN, TEABLE_URL


class TeableService:
    """Service for interacting with the Teable API."""

    def __get_headers(self) -> dict[str, str]:
        """
        Generate HTTP headers for Teable API requests.

        Returns:
            A dictionary containing the authorization bearer token.
        """
        return {'Authorization': f'Bearer {TEABLE_API_TOKEN}'}

    def read(self, table_id: str) -> dict:
        """
        Retrieve records from a specified table.

        Args:
            table_id: The ID of the table to read.

        Returns:
            The JSON response from the Teable API.
        """
        url = f'{TEABLE_URL}/api/table/{table_id}/record'
        response = requests.get(url, headers=self.__get_headers(), timeout=10)
        response.raise_for_status()
        return response.json()

    def add(self, table_id, **kwargs):
        url = f'{TEABLE_URL}/api/table/{table_id}/record'
        data = {"fieldKeyType": "name", "records": [{"fields": kwargs}]}
        response = requests.post(url,
                                 headers=self.__get_headers(),
                                 json=data,
                                 timeout=10)
        response.raise_for_status()
        return response.json()
