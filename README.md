[![codecov](https://codecov.io/github/rawandahmad698/fib-python-payment-sdk/branch/main/graph/badge.svg?token=1GRCQ2FO0F)](https://codecov.io/github/rawandahmad698/fib-python-payment-sdk)

# FIB Payment SDK

The FIB Payment SDK provides seamless integration with the FIB payment system, empowering developers to streamline
payment transactions and facilitate secure refunds within their applications.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
    - [Using pip](#using-pip)
    - [Alternative Installation (Without pip)](#alternative-installation-without-pip)
- [Configuration](#configuration)
- [Usage of the SDK](#usage-of-the-sdk)
    - [Payment Integration Examples](#payment-integration-examples)
- [Documentation](#documentation)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)
- [Acknowledgments](#acknowledgments)
- [Versioning](#versioning)
- [FAQ](#faq)

---

## Features

- **Payment Transactions**: Enable users to make payments securely through the FIB payment system.
- **Refund Processing**: Process refunds securely and efficiently.
- **Payment Status Checking**: Track the status of payments accurately.
- **Payment Cancellation**: Cancel payments securely and easily.

---

## Installation

Install the SDK using pip:

```bash
pip install fib-python-payment-sdk
```

### Alternative Installation (Without pip)

You can clone the repository and manually include the SDK in your project:

```bash
git clone https://github.com/First-Iraqi-Bank/fib-python-payment-sdk.git
```

Ensure to include the SDK directory in your Python path.

---

### Configuration

Set the following environment variables to configure the SDK:

- `FIB_API_KEY`: Your FIB payment API key.
- `FIB_API_SECRET`: Your FIB payment API secret.
- `FIB_BASE_URL`: Base URL for the FIB payment API.
- `FIB_GRANT_TYPE`: Authentication grant type (default: client_credentials).
- `FIB_REFUNDABLE_FOR`: Transaction refund period (default: P7D).
- `FIB_CURRENCY`: Transaction currency (default: IQD).
- `FIB_CALLBACK_URL`: Callback URL for handling payment notifications.

---

### Usage of the SDK

Below is a basic example of how to use the SDK to handle payment operations directly within your application.

#### Payment Operations Example

This example demonstrates how to perform common payment operations, including creating a payment, checking its status,
issuing a refund, and canceling a payment.

1. **Setup Environment Variables**:
   Ensure you have loaded the necessary environment variables for the SDK.

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from the .env file
   load_dotenv()
   ```

2. **Full example**:
      Below is a full example of how to use the SDK to handle payment operations:

      ```python
      import asyncio
      from fib_payments import FIBPaymentsClient, FIBConfig, APIError

      async def main():
          config = FIBConfig(
              base_url="https://fib.dev.fib.iq",
              client_id="your token",
              client_secret="your secret"
          )
   
          # or config = FIBConfig()
         async with FIBPaymentsClient(config) as client:
           try:
               # Create a payment
               payment = await client.create_payment(100.00, description="Test payment")
               payment_details = {
                  'fib_payment_id': payment['paymentId'],
                  'readable_code': payment['readableCode'],
                  'personal_app_link': payment['personalAppLink'],
                  'valid_until': payment['validUntil'],
              }
               print(f"Payment created: {payment_details}")

               # Check payment status
               status = await client.get_payment_status(payment['paymentId'])
               print(f"Payment status: {status}")

               # Refund the payment
               refund = await client.refund_payment(payment['paymentId'])
               print(f"Refund initiated: {refund}")

           except APIError as e:
               print(f"An API error occurred: {str(e)}")
      ```


---

### Documentation

For more detailed documentation, refer to
the [FIB Online Payment API Documentation](https://documenter.getpostman.com/view/18377702/UVCB93tc).

---

### Testing

Run the SDK tests using `unittest`:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Run a specific test case:

```bash
python -m unittest tests.test_module.TestClassName
```

Run a specific test method:

```bash
python -m unittest tests.test_module.TestClassName.test_method_name
```

To run tests with custom formatting, use:

```bash
python test.py
```

---

### Contributing

Contributions are welcome! Please refer to the `CONTRIBUTING.md` for guidelines.

---

### License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

---

### Support

For support, contact support@fib-payment.com.

---

### Acknowledgments

Thanks to the FIB Payment development team and the `requests` library.

---

### Versioning

We follow [Semantic Versioning](https://semver.org/) for releases.

---

### FAQ

**Q: How do I get an API key for the FIB Payment system?**

A: Contact support@fib-payment.com to request an API key.

**Q: Can I use this SDK in production?**

A: Yes, but ensure it is correctly configured and tested for your environment.


