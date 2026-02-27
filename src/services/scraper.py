import re

from bs4 import BeautifulSoup

from utils.text import TextUtils


class ScraperService:

    def __init__(self):
        self.text_utils = TextUtils()

    def bac(self, html_raw_text):
        result = {}
        content = ""

        html_raw_text = self.text_utils.normalize_text(
            html_raw_text.replace("\n", ""))

        soup = BeautifulSoup(html_raw_text, "html.parser")

        html_text_tags = soup.find_all("p")

        for tag in html_text_tags:
            content += tag.text + "$%"

        pattern = r"(?:([A-z ]+):|(AMEX|VISA|MASTER))\$\%(.+?)\$\%"

        matches = re.findall(pattern, content, re.DOTALL)

        for match in matches:
            key = match[0] if match[0] else match[1]
            value = match[2].strip()

            if key:
                result[key] = value
        return result
