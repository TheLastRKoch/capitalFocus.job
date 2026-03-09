import base64


def base_64_decode(encoded_text: str) -> str:
    """
    Decode a base64 encoded string into UTF-8 text.

    Args:
        encoded_text (str): The input string encoded in base64.

    Returns:
        str: The decoded plain text string.
    """
    return base64.urlsafe_b64decode(encoded_text).decode('utf-8',
                                                         errors='replace')
