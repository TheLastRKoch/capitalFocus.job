from services.bac_parser import BACParserService
from services.gmail import GmailService

# define services
bac_parser = BACParserService()
gmail = GmailService()

try:
    email_list = gmail.get_email_list("label:job-new")["messages"]

    print(f'Found {len(email_list)} emails to process')
    for email in email_list:
        message = gmail.get_message(email["id"])
        text, html = gmail.get_email_content(message)
        print(text)
        operation_type = bac_parser.get_operation_type(text)
        print(f'selected {operation_type}')
        match operation_type:
            case operation_type.TRANSACTION:
                data = bac_parser.scrape_transaction(html)
                validation_result = bac_parser.validate(
                    data, bac_parser.transaction_schema)
                if not validation_result:
                    raise Exception(
                        "Error the data did not pass the validation")
            case operation_type.TRANSFER:
                data = bac_parser.scrape_transfer(html)
                validation_result = bac_parser.validate(
                    data, bac_parser.transfer_schema)
                if not validation_result:
                    raise Exception(
                        "Error the data did not pass the validation")
        print(data)
except Exception as error:
    print(f"something went wrong {error}")
    # TODO: Move the email to the error label
