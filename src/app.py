from services.bac_parser import BACParserService
from services.gmail import GmailService

bac_parser = BACParserService()
gmail = GmailService()

email_list = gmail.get_email_list("label:job-new")["messages"]

print(f'Found {len(email_list)} emails to process')
for email in email_list:
    message = gmail.get_message(email["id"])
    text, html = gmail.get_email_content(message)
    operation_type = bac_parser.get_operation_type(text)
    print(f'selected {operation_type.__name__}')
    print(operation_type(html))
