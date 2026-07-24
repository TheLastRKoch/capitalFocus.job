from parsers.factory import FactoryParser
from services.gmail import GmailService
from services.validator import ValidatorService
from repositories.transactions import TransactionsRepository
import traceback
import logging
import json

logger = logging.getLogger(__name__)


def process_email(email_id: str, gmail_service: GmailService,
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
    message = gmail_service.get_message(email_id)
    if not message:
        return

    subject = gmail_service.get_email_subject(message)
    logging.info("Start processing email: "+subject)

    text, html = gmail_service.get_email_content(message)
    logger.debug("Retrieved text: "+text)
    logger.debug("Retrieved HTML: "+html)

    operation_type = parser_factory.get_operation_type(text)
    logger.info(f'Selected operation type: {operation_type}')

    if not operation_type:
        raise Exception('Could not determine operation type of the email.')

    parser = parser_factory.get_parser(operation_type)
    data = parser.parse(html)

    schema_path = f'src/schemas/{operation_type.name.lower()}.json'
    validator = ValidatorService(schema_path)

    logger.debug('Processed data:', data)

    if not validator.validate(data):
        raise ValueError('Data validation failed.')

    logger.info('Passed validation')

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

    transaction_repo.submit([transaction_data])
    logging.info("Stop processing email: "+subject)



def main():
    """
    Main function to process emails.
    """
    gmail_service = GmailService()
    parser_factory = FactoryParser()
    transaction_repo = TransactionsRepository()

    email_list_response = gmail_service.get_email_list('label:job-new')
    email_list = email_list_response.get('messages', [])
    logger.info(f'Found {len(email_list)} emails to process')

    logging.info("Process start")

    try:
        for email in email_list:
            process_email(email['id'], gmail_service, parser_factory,
                          transaction_repo)
            gmail_service.move_to_label(email.get('id'), 'Job/Processed')

    except Exception as error:
        logging.error(f'Error processing email {error} {traceback.print_exc()}')
        gmail_service.move_to_label(email.get('id'), 'Job/Error')

    finally:
        logging.info("Process end\n\n")


if __name__ == '__main__':
    main()
