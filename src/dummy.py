from services.scraper import ScraperService
import json

scraper = ScraperService()

html_raw_text = ""

with open("view.html", "r") as file:
    html_raw_text = file.read()

result = scraper.bac(html_raw_text)
print(json.dumps(result, indent=4))
