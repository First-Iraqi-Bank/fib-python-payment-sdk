from examples.fib_payment_operations import create_payment, cancel_payment

# Create a new payment
payment_details = create_payment(1000, 'http://localhost/callback', 'Test payment description')

if payment_details:
    # Check payment status using the created payment ID
    payment_id = payment_details['fib_payment_id']
    cancel_status_code = cancel_payment(payment_id)
    print("Cancel Status Code:", cancel_status_code)
else:
    print("Failed to create payment.")
