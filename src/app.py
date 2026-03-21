from services.bac_parser import BACParserFactory, OperationType
from services.gmail import GmailService
from services.validator import ValidatorService


def process_email(email_id: str, gmail_service: GmailService, parser_factory: BACParserFactory):
    """
    Processes a single email.

    Args:
        email_id: The ID of the email to process.
        gmail_service: The Gmail service instance.
        parser_factory: The parser factory instance.
    """
    message = gmail_service.get_message(email_id)
    text, html = gmail_service.get_email_content(message)
    print(text)

    operation_type = parser_factory.get_operation_type(text)
    print(f'Selected operation type: {operation_type}')

    if not operation_type:
        print("Could not determine operation type. Skipping email.")
        return

    try:
        parser = parser_factory.get_parser(operation_type)
        data = parser.parse(html)

        schema_path = f"src/schemas/{operation_type.name.lower()}.json"
        validator = ValidatorService(schema_path)

        if not validator.validate(data):
            raise Exception("Data validation failed.")

        print("Processed data:", data)

    except Exception as e:
        print(f"Error processing email {email_id}: {e}")
        # TODO: Move the email to the error label


def main():
    """
    Main function to process emails.
    """
    gmail_service = GmailService()
    parser_factory = BACParserFactory()

    try:
        email_list = gmail_service.get_email_list("label:job-new")["messages"]
        print(f'Found {len(email_list)} emails to process')

        for email in email_list:
            process_email(email["id"], gmail_service, parser_factory)

    except Exception as error:
        print(f"Something went wrong: {error}")


if __name__ == "__main__":
    main()
