Here's an updated version of your SDK documentation with the integration examples and payment operations files added:

---

# FIB Payment SDK

The FIB Payment SDK provides seamless integration with the FIB payment system, empowering developers to streamline payment transactions and facilitate secure refunds within their applications.

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

Got it! You want to include the functionality as part of the SDK usage examples in the documentation, without referencing an actual file. Here’s how you can structure that:

---

### Usage of the SDK

Below is a basic example of how to use the SDK to handle payment operations directly within your application.

#### Payment Operations Example

This example demonstrates how to perform common payment operations, including creating a payment, checking its status, issuing a refund, and canceling a payment.

1. **Setup Environment Variables**:
   Ensure you have loaded the necessary environment variables for the SDK.

   ```python
   from dotenv import load_dotenv
   import os

   # Load environment variables from the .env file
   load_dotenv()
   ```

2. **Initialize Services**:
   Create instances of the authentication and payment integration services.

   ```python
   from fib_python_payment_sdk.services.fib_auth_integration_service import FIBAuthIntegrationService
   from fib_python_payment_sdk.services.fib_payment_integration_service import FIBPaymentIntegrationService

   # Initialize the authentication service
   auth_service = FIBAuthIntegrationService()

   # Initialize the payment integration service
   payment_service = FIBPaymentIntegrationService(auth_service)
   ```

3. **Create a Payment**:

   To create a payment, use the following function:

   ```python
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
   ```

   Example usage:

   ```python
   payment_details = create_payment(1000, 'http://localhost/callback', 'Test payment description')
   print("Payment Details:", payment_details)
   ```

4. **Check Payment Status**:

   To check the status of a payment:

   ```python
   def check_payment_status(payment_id):
       try:
           status = payment_service.check_payment_status(payment_id)
           return status
       except Exception as e:
           print("Error during payment status check:", str(e))
           return None
   ```

   Example usage:

   ```python
   if payment_details:
       payment_id = payment_details['fib_payment_id']
       status = check_payment_status(payment_id)
       print("Payment Status:", status)
   ```

5. **Refund a Payment**:

   To refund a payment:

   ```python
   def refund_payment(payment_id):
       try:
           refund_response = payment_service.refund(payment_id)
           return refund_response.status_code
       except Exception as e:
           print("Error during refund:", str(e))
           return None
   ```

   Example usage:

   ```python
   if payment_details:
       payment_id = payment_details['fib_payment_id']
       refund_status_code = refund_payment(payment_id)
       print("Refund Status Code:", refund_status_code)
   ```

6. **Cancel a Payment**:

   To cancel a payment:

   ```python
   def cancel_payment(payment_id):
       try:
           cancel_response = payment_service.cancel(payment_id)
           return cancel_response.status_code
       except Exception as e:
           print("Error during cancellation:", str(e))
           return None
   ```

   Example usage:

   ```python
   if payment_details:
       payment_id = payment_details['fib_payment_id']
       cancel_status_code = cancel_payment(payment_id)
       print("Cancel Status Code:", cancel_status_code)
   ```

---

This structure provides clear examples of how to use the SDK for payment operations, focusing on practical usage rather than code organization in a specific file.



---

### Documentation

For more detailed documentation, refer to the [FIB Online Payment API Documentation](https://documenter.getpostman.com/view/18377702/UVCB93tc).

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

---

This adds the example files to your documentation and explains how to use them effectively.