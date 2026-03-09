from enviroment import TEABLE_API_TOKEN, TEABLE_URL

import requests


class TeableService:

    def __get_headers(self):
        return {'Authorization': 'Bearer ' + TEABLE_API_TOKEN}

    def read(self, table_id):

        url = f"{TEABLE_URL}/api/table/{table_id}/record"

        response = requests.request(
            "GET",
            url,
            headers=self.__get_headers(),
        )

        response.raise_for_status()
        return response.json()
