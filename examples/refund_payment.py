from examples.fib_payment_operations import create_payment, refund_payment

# Create a new payment
payment_details = create_payment(1000, 'http://localhost/callback', 'Test payment description')

if payment_details:
    # Check payment status using the created payment ID
    payment_id = payment_details['fib_payment_id']
    refund_status_code = refund_payment(payment_id)
    print("Refund Status Code:", refund_status_code)
else:
    print("Failed to create payment.")
