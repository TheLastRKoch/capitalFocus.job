import unicodedata


class TextUtils:
    """Utility class for text processing."""

    def normalize_text(self, text: str) -> str:
        """
        Normalize text to remove non-spacing marks (e.g., accents).

        Args:
            text (str): The input text to be normalized.

        Returns:
            str: The normalized text.
        """
        proceed_text = unicodedata.normalize('NFD', text)
        return ''.join(c for c in proceed_text
                       if unicodedata.category(c) != 'Mn')
