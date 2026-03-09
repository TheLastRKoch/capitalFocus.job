import unittest
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
                    and the value is a tuple representing the sequential keys to traverse.
                    Example: {'employee_name': ('company', 'hr', 'name')}
        """
        self.schema = schema

    def _resolve(self, data: Any, path: Tuple[str, ...]) -> Any:
        """
        Traverse the nested dictionary along the given path.
        Returns None if a key is missing or the path is broken.
        """
        return reduce(lambda d, k: d.get(k) if isinstance(d, dict) else None, path, data)

    def transform(self, source_json: Dict[str, Any]) -> Dict[str, Any]:
        """
        Transform a single JSON object based on the schema.
        """
        return {new_key: self._resolve(source_json, path) 
                for new_key, path in self.schema.items()}

    def transform_batch(self, source_json_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Transform a list of JSON objects based on the schema.
        """
        return [self.transform(item) for item in source_json_list]


def bac(scraped_json):
    [
        {""}
    ]


class TestJsonMapper(unittest.TestCase):
    
    def test_case_a_deep_nesting(self) -> None:
        """Case A (Deep Nesting)"""
        schema = {"target": ("a", "b", "c")}
        mapper = JsonMapperService(schema)
        input_data = {"a": {"b": {"c": "success"}}}
        expected = {"target": "success"}
        self.assertEqual(mapper.transform(input_data), expected)

    def test_case_b_short_nesting(self) -> None:
        """Case B (Short Nesting)"""
        schema = {"target": ("user", "id")}
        mapper = JsonMapperService(schema)
        input_data = {"user": {"id": 101}}
        expected = {"target": 101}
        self.assertEqual(mapper.transform(input_data), expected)

    def test_case_c_missing_key(self) -> None:
        """Case C (Missing Key)"""
        schema = {"target": ("company", "rank")}
        mapper = JsonMapperService(schema)
        input_data = {"company": {"name": "Test"}}
        expected = {"target": None}
        self.assertEqual(mapper.transform(input_data), expected)
        
    def test_case_d_broken_path_type_error_prevention(self) -> None:
        """Ensure type errors are prevented when path traverses a non-dict element."""
        schema = {"target": ("user", "id", "nested")}
        mapper = JsonMapperService(schema)
        # user.id is an int, so trying to get "nested" from it should just safely return None
        input_data = {"user": {"id": 101}}
        expected = {"target": None}
        self.assertEqual(mapper.transform(input_data), expected)

    def test_transform_batch(self) -> None:
        """Test processing a list of JSON objects."""
        schema = {
            "name": ("employee", "name"),
            "department": ("employee", "dept"),
            "role": ("role",)
        }
        mapper = JsonMapperService(schema)
        
        input_data = [
            {"employee": {"name": "Alice", "dept": "Engineering"}, "role": "Senior"},
            {"employee": {"name": "Bob"}, "role": "Junior"},
            {"other_format": {"employee": "Charlie"}} # Missing expected structure
        ]
        
        expected = [
            {"name": "Alice", "department": "Engineering", "role": "Senior"},
            {"name": "Bob", "department": None, "role": "Junior"},
            {"name": None, "department": None, "role": None}
        ]
        self.assertEqual(mapper.transform_batch(input_data), expected)


if __name__ == '__main__':
    unittest.main()
