# from services.scraper import ScraperService
# import json

# scraper = ScraperService()

# html_raw_text = ""

# with open("view.html", "r") as file:
#     html_raw_text = file.read()

# result = scraper.bac(html_raw_text)
# print(json.dumps(result, indent=4))

from services.gmail import GmailService

gmail = GmailService()

email_list = gmail.get_email_list("label:job-new")["messages"]

for email in email_list:
    email = gmail.get_email(email["id"])
    text, html = gmail.def_get_email_content(email)
    print(text)
    print(html)
    breakpoint()
