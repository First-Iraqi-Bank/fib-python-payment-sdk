from dotenv import load_dotenv

from src.fib_python_payment_sdk.services.fib_auth_integration_service import FIBAuthIntegrationService
from src.fib_python_payment_sdk.services.fib_payment_integration_service import FIBPaymentIntegrationService

# Load environment variables from the .env file
load_dotenv()

# Initialize the authentication service
auth_service = FIBAuthIntegrationService()

# Initialize the payment integration service
payment_service = FIBPaymentIntegrationService(auth_service)


def create_payment(amount, callback_url, description):
    try:
        payment_response = payment_service.create_payment(amount, callback_url, description)
        payment_details = {
            'fib_payment_id': payment_response['paymentId'],
            'readable_code': payment_response['readableCode'],
            'personal_app_link': payment_response['personalAppLink'],
            'valid_until': payment_response['validUntil'],
        }
        return payment_details
    except Exception as e:
        print("Error during payment creation:", str(e))
        return None


def check_payment_status(payment_id):
    try:
        status = payment_service.check_payment_status(payment_id)
        return status
    except Exception as e:
        print("Error during payment status check:", str(e))
        return None


def refund_payment(payment_id):
    try:
        refund_response = payment_service.refund(payment_id)
        return refund_response.status_code
    except Exception as e:
        print("Error during refund:", str(e))
        return None


def cancel_payment(payment_id):
    try:
        cancel_response = payment_service.cancel(payment_id)
        return cancel_response.status_code
    except Exception as e:
        print("Error during cancellation:", str(e))
        return None
