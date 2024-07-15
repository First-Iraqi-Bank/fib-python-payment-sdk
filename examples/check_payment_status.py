from examples.fib_payment_operations import create_payment, check_payment_status

# Create a new payment
payment_details = create_payment(1000, 'http://localhost/callback', 'Test payment description')

if payment_details:
    # Check payment status using the created payment ID
    payment_id = payment_details['fib_payment_id']
    status = check_payment_status(payment_id)
    print("Payment Status:", status)
else:
    print("Failed to create payment.")
