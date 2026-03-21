from jsonschema import validate, ValidationError

class Validator:
    def validate_json(self, data, schema):
        """
        Validates a JSON-like object against a given schema.

        Args:
            data (dict): The JSON-like object (Python dictionary) to validate.
            schema (dict): The JSON schema to validate against.

        Returns:
            bool: True if the data is valid, False otherwise.
            str: A message indicating validation success or failure.
        """
        try:
            validate(instance=data, schema=schema)
            return True, "Valid!"
        except ValidationError as e:
            return False, f"Invalid data: {e.message}"
