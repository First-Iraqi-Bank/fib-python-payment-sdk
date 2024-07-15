from dotenv import load_dotenv

import os
from fib_python_payment_sdk.services.fib_auth_integration_service import FIBAuthIntegrationService
from fib_python_payment_sdk.services.fib_payment_integration_service import FIBPaymentIntegrationService


# Load environment variables from the .env file
load_dotenv()

# Initialize the authentication service
auth_service = FIBAuthIntegrationService()

# Initialize the payment integration service
payment_service = FIBPaymentIntegrationService(auth_service)

try:
    # Create a new payment
    payment_response = payment_service.create_payment(1000, 'http://localhost/callback', 'Test payment description')

    # Payment details
    payment_details = {
        'fib_payment_id': payment_response['paymentId'],
        'readable_code': payment_response['readableCode'],
        'personal_app_link': payment_response['personalAppLink'],
        'valid_until': payment_response['validUntil'],
    }

    print("Payment Details:")
    print("FIB Payment ID:", payment_details['fib_payment_id'])
    print("Readable Code:", payment_details['readable_code'])
    print("Personal App Link:", payment_details['personal_app_link'])
    print("Valid Until:", payment_details['valid_until'])
    print("\n" * 1)

    # Check Payment Status
    payment_id = payment_details['fib_payment_id']
    status = payment_service.check_payment_status(payment_id)
    print("Payment Status:", status)
    print("\n" * 1)

    # Refund Payment
    refund_response = payment_service.refund(payment_id)
    print("Refund Status Code:", refund_response.status_code)
    print("\n" * 1)

    # Cancel Payment
    cancel_response = payment_service.cancel(payment_id)
    print("Cancel Status Code:", cancel_response.status_code)

    # Handling Payment Callbacks,
    # This would typically be implemented in your web application where the callback URL receives POST requests
    # Example:
    # payment_id = request.form['id']
    # status = request.form['status']
    # payment_service.handle_callback(payment_id, status)

except Exception as e:
    print("Error:", str(e))
