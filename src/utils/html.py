from bs4 import BeautifulSoup
from utils.text import TextUtils


class HtmlUtils:
    """A utility class for HTML processing."""

    @staticmethod
    def extract_content_from_html(html_raw_text: str, tag_query: str) -> str:
        """
        Parses raw HTML and extracts text content from specified tags.

        Args:
            html_raw_text: The raw HTML string to process.
            tag_query: The HTML tag to query for text extraction.

        Returns:
            The extracted and concatenated text content.
        """
        text_utils = TextUtils()
        normalized_html = text_utils.normalize_text(html_raw_text.replace("
", ""))
        soup = BeautifulSoup(normalized_html, "html.parser")
        html_text_tags = soup.find_all(tag_query)
        return "".join(f"{tag.text}$%" for tag in html_text_tags)
