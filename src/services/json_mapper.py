from typing import Any, Dict, List, Tuple, Union


class JsonMapperService:
    """
    A utility class that maps disparate, nested JSON structures into a unified,
    flat dictionary based on user-defined tuple paths.
    """

    def __init__(self, schema: Dict[str, Union[str, Tuple[str, ...]]]) -> None:
        """
        Initialize with a mapping schema.

        Args:
            schema: A dictionary where the key is the desired output field name
                    and the value is a string or tuple representing the sequential keys.
        """
        self.schema = schema

    def _resolve(self, data: Any, path: Union[str, Tuple[str, ...]]) -> Any:
        """
        Traverse the nested dictionary along the given path.
        """
        if not data:
            return None

        if isinstance(path, str):
            return data.get(path)

        if isinstance(path, tuple):
            for key in path:
                if not isinstance(data, dict):
                    return None
                data = data.get(key)
                if data is None:
                    break
            return data
        return None

    def transform(self, source_json: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform a single JSON object based on the schema.
        """
        result = {}
        for new_key, path in self.schema.items():
            value = self._resolve(source_json, path)
            if value is not None:
                result[new_key] = value
        return result

    def transform_batch(
            self, source_json_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform a list of JSON objects based on the schema.
        """
        return [self.transform(item) for item in source_json_list]
