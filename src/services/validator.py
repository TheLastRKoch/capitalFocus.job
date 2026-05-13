import json
from typing import Dict, Any
from jsonschema import validate, ValidationError


class ValidatorService:
    """A service for validating data against JSON schemas."""

    def __init__(self, schema_path: str) -> None:
        """Initializes the ValidatorService with a schema."""
        self.schema = self._load_schema(schema_path)

    def _load_schema(self, schema_path: str) -> Dict[str, Any]:
        """Loads a JSON schema from a file."""
        with open(schema_path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def validate(self, data: Dict[str, Any]) -> bool:
        """
        Validates data against the loaded schema.

        Args:
            data: The data to validate.

        Returns:
            True if the data is valid, False otherwise.
        """
        try:
            validate(instance=data, schema=self.schema)
            return True
        except ValidationError as e:
            print(f'Validation Error: {e.message}')
            return False
