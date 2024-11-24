import asyncio
from fib_payments import FIBPaymentsClient, FIBConfig, APIError


async def main():
    config = FIBConfig(
        base_url="https://fib.dev.fib.iq",
        client_id="your token",
        client_secret="your secret"
    )

    # or
    """ 
    config = FIBConfig()
    """

    async with FIBPaymentsClient(config) as client:
        try:
            # Create a payment
            payment = await client.create_payment(100.00, description="Test payment")
            print(f"Payment created: {payment}")

            # Check payment status
            status = await client.get_payment_status(payment['paymentId'])
            print(f"Payment status: {status}")

            # Refund the payment
            refund = await client.refund_payment(payment['paymentId'])
            print(f"Refund initiated: {refund}")

        except APIError as e:
            print(f"An API error occurred: {str(e)}")


asyncio.run(main())
