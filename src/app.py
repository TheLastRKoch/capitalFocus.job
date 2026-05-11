from parsers.factory import FactoryParser
from services.gmail import GmailService
from services.validator import ValidatorService
from repositories.transactions import TransactionsRepository
import json


def process_email(email_id: str, gmail_service: GmailService,
                  parser_factory: FactoryParser, transaction_repo):
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
        print('Could not determine operation type. Skipping email.')
        return

    try:
        parser = parser_factory.get_parser(operation_type)
        data = parser.parse(html)

        schema_path = f'src/schemas/{operation_type.name.lower()}.json'
        validator = ValidatorService(schema_path)

        print('Processed data:', data)

        if not validator.validate(data):
            raise Exception('Data validation failed.')

        print('Passed validation')

        json_mapped = parser.mapper(data)

        transaction_repo.add(
            date=json_mapped.get('date'),
            commerce=json_mapped.get('commerce'),
            amount=json_mapped.get('amount'),
            location=json_mapped.get('location'),
            card=json_mapped.get('card'),
            authorization=json_mapped.get('authorization'),
            reference=json_mapped.get('reference'),
            transactionType=json_mapped.get('transactionType'),
            status=json_mapped.get('status'),
            json=json.dumps(data),
            html=html,
        )

    except Exception as e:
        print(f'Error processing email {email_id}: {e}')
        # TODO: Move the email to the error label


def main():
    """
    Main function to process emails.
    """
    gmail_service = GmailService()
    parser_factory = FactoryParser()
    transaction_repo = TransactionsRepository()

    try:
        email_list = gmail_service.get_email_list('label:job-new')['messages']
        print(f'Found {len(email_list)} emails to process')

        for email in email_list:
            process_email(email['id'], gmail_service, parser_factory,
                          transaction_repo)

    except Exception as error:
        print(f'Something went wrong: {error}')


if __name__ == '__main__':
    main()
