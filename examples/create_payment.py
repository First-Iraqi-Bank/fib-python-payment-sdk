from examples.fib_payment_operations import create_payment

payment_details = create_payment(1000, 'http://localhost/callback', 'Test payment description')

if payment_details:
    print("Payment Details:")
    print("FIB Payment ID:", payment_details['fib_payment_id'])
    print("Readable Code:", payment_details['readable_code'])
    print("Personal App Link:", payment_details['personal_app_link'])
    print("Valid Until:", payment_details['valid_until'])
else:
    print("Failed to create payment.")
