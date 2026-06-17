from parsers.factory import FactoryParser
from services.gmail import GmailService
from services.validator import ValidatorService
from repositories.transactions import TransactionsRepository
import json


def process_email(email, gmail_service: GmailService,
                  parser_factory: FactoryParser,
                  transaction_repo: TransactionsRepository):
    """
    Processes a single email.

    Args:
        email_id: The ID of the email to process.
        gmail_service: The Gmail service instance.
        parser_factory: The parser factory instance.
        transaction_repo: The transaction repository instance.
    """
    message = gmail_service.get_message(email.get('id'))
    if not message:
        return

    text, html = gmail_service.get_email_content(message)
    print(text)

    operation_type = parser_factory.get_operation_type(text)
    print(f'Selected operation type: {operation_type}')

    if not operation_type:
        raise Exception('Could not determine operation type of the email.')

    try:
        parser = parser_factory.get_parser(operation_type)
        data = parser.parse(html)

        schema_path = f'src/schemas/{operation_type.name.lower()}.json'
        validator = ValidatorService(schema_path)

        print('Processed data:', data)

        if not validator.validate(data):
            raise ValueError('Data validation failed.')

        print('Passed validation')

        json_mapped = parser.mapper(data)

        # Ensure all required fields are present with defaults
        transaction_data = {
            'date': json_mapped.get('date'),
            'commerce': json_mapped.get('commerce'),
            'amount': json_mapped.get('amount'),
            'location': json_mapped.get('location'),
            'card': json_mapped.get('card'),
            'authorization': json_mapped.get('authorization'),
            'reference': json_mapped.get('reference'),
            'transactionType': json_mapped.get('transactionType'),
            'status': json_mapped.get('status'),
            'json': json.dumps(data),
            'html': html,
        }

        transaction_repo.add(**transaction_data)
        gmail_service.move_to_label(email.get('id'), 'Job/Processed')

    except Exception as error:
        gmail_service.move_to_label(email.get('id'), 'Job/Error')
        print(f'Something went wrong: {error}')


def main():
    """
    Main function to process emails.
    """
    gmail_service = GmailService()
    parser_factory = FactoryParser()
    transaction_repo = TransactionsRepository()

    email_list_response = gmail_service.get_email_list('label:job-new')
    email_list = email_list_response.get('messages', [])
    print(f'Found {len(email_list)} emails to process')

    for email in email_list:
        process_email(email, gmail_service, parser_factory, transaction_repo)


if __name__ == '__main__':
    main()
