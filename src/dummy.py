# # html_raw_text = ""

# # with open("view.html", "r") as file:
# #     html_raw_text = file.read()

from services.scraper import ScraperService
from services.gmail import GmailService
import json

scraper = ScraperService()
gmail = GmailService()

email_list = gmail.get_email_list("label:job-new")["messages"]

for email in email_list:
    message = gmail.get_message(email["id"])

    # file_path = get_unique_filepath("message.json")
    # with open(file_path, "w") as file:
    #     file.write(json.dumps(message, indent=4))

    text, html = gmail.get_email_content(message)
    print(scraper.bac_transfer(html))
