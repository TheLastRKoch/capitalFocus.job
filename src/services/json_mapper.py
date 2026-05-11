from functools import reduce
from typing import Any, Dict, List, Tuple


class JsonMapperService:
    """
    A utility class that maps disparate, nested JSON structures into a unified,
    flat dictionary based on user-defined tuple paths.
    """

    def __init__(self, schema: Dict[str, Tuple[str, ...]]) -> None:
        """
        Initialize with a mapping schema.

        Args:
            schema: A dictionary where the key is the desired output field name
                    and the value is a tuple representing the sequential keys.
        """
        self.schema = schema

    def _resolve(self, data: Any, path: Tuple[str, ...]) -> Any:
        """
        Traverse the nested dictionary along the given path.
        """
        return reduce(lambda d, k: d.get(k)
                      if isinstance(d, dict) else None, path, data)

    def transform(self, source_json: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform a single JSON object based on the schema.
        """
        return {
            new_key: self._resolve(source_json, path)
            for new_key, path in self.schema.items()
        }

    def transform_batch(
            self, source_json_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform a list of JSON objects based on the schema.
        """
        return [self.transform(item) for item in source_json_list]
