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

- **Payment Transactions**: Enable users to make payments securely through the FIB payment system, handling transactions effortlessly within your application.
- **Refund Processing**: Process refunds securely through the FIB payment system, managing transactions efficiently within your application.
- **Payment Status Checking**: Check the status of payments to ensure accurate transaction tracking.
- **Payment Cancellation**: Cancel payments securely through the FIB payment system, providing flexibility and control over payment transactions.

---

## Installation

To integrate the SDK into your project, You can install a package directly from its GitHub repository using the following command:

```bash
pip install git+https://github.com/First-Iraqi-Bank/fib-python-payment-sdk

```

## Alternative Installation (Without pip)
If your project prefers not to use pip for dependency management, you can manually include the FIB Payment SDK by following these steps:

- Clone the Repository: Clone the FIB Payment SDK repository directly into your project directory or any preferred
  location:

```bash
git clone https://github.com/First-Iraqi-Bank/fib-python-payment-sdk.git
```

- Include in Your Project:
  Copy or move the cloned `fib-python-payment-sdk` directory into your project structure. You can place it wherever it suits your project best.

- Autoloading (if applicable):
  Ensure that the SDK directory is included in your Python path. You might do this by adding the directory to your `PYTHONPATH` or by using a virtual environment.

- Usage: After including the SDK in your project, you can use its classes and functionalities directly in your Python
  files.

### Notes
- Ensure that the SDK repository URL (https://github.com/First-Iraqi-Bank/fib-python-payment-sdk.git) is correct and
  accessible.
- Manually managing dependencies may require additional effort to keep the SDK updated with the latest changes and
  fixes.
- Consider using pip for managing dependencies whenever possible, as it simplifies dependency management and
  ensures compatibility with other packages.

---

### Configuration

To configure the SDK, you need to set the following environment variables:

- `FIB_API_KEY`: Your FIB payment API key.
- `FIB_API_SECRET`: Your FIB payment API secret.
- `FIB_BASE_URL`: The base URL for the FIB payment API (default: https://api.fibpayment.com).
- `FIB_GRANT_TYPE`: The grant type for authentication with the FIB payment API (default: client_credentials).
- `FIB_REFUNDABLE_FOR`: The period for which transactions can be refunded (default: P7D, which stands for 7 days).
- `FIB_CURRENCY`: The currency used for transactions with the FIB payment system (default: IQD).
- `FIB_CALLBACK_URL`: The callback URL for handling payment notifications from the FIB payment system.
- `FIB_ACCOUNT`: The FIB payment account identifier.

Make sure to set these environment variables appropriately in your application's environment configuration.

---

### Usage of the SDK

Below is a basic example of how to use the SDK:

#### Ensure Dependencies are Installed:
Make sure you have installed all required dependencies using pip:
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables:
Create a `.env` file in the root directory of your project and configure the necessary environment variables. Refer to the `.env.example` file for the required variables.

Certainly! Here's a documentation section for your README.md file that explains how to use the payment integration examples:

---

### Payment Integration Examples

#### Overview

This section provides examples of integrating with the FIB payment system using the Python SDK. The examples demonstrate various operations such as creating payments, checking payment status, refunding payments, and canceling payments.

#### Running the Examples

1. **Creating a Payment:**

   The example demonstrates how to create a new payment and retrieve its details.

   ```bash
   python create_payment.py
   ```

   This script initializes the payment integration service and creates a new payment with a specified amount, callback URL, and description.

2. **Checking Payment Status:**

   Use the following script to check the status of a previously created payment:

   ```bash
   python check_payment_status.py
   ```

   Replace `"your_payment_id_here"` with the actual payment ID received from the create payment operation.

3. **Refunding a Payment:**

   To refund a payment, execute the following script:

   ```bash
   python refund_payment.py
   ```

   Replace `"your_payment_id_here"` with the actual payment ID received from the create payment operation.

4. **Canceling a Payment:**

   Use this script to cancel a payment by its ID:

   ```bash
   python cancel_payment.py
   ```

   Replace `"your_payment_id_here"` with the actual payment ID received from the create payment operation.

#### Error Handling

Each example includes basic error handling to catch and print any exceptions that may occur during the execution of API calls.

---

### FIB Payment Documentation

For comprehensive details on FIB Online Payment, please refer to the [full documentation](https://documenter.getpostman.com/view/18377702/UVCB93tc).


---

### Testing

To ensure the SDK functions correctly, ensure Python and necessary dependencies are installed:

#### Running Tests:
Navigate to the directory containing your SDK. Use the following command to run tests
```bash
   python -m unittest discover -s tests -p 'test_*.py'
```

#### Run a Specific Test Case
To run a specific test case from a module using unittest:
```bash
  python -m unittest tests.test_module.TestClassName
```

#### Run a Specific Test Method
To run a specific test method within a test case:
```bash
  python -m unittest tests.test_module.TestClassName.test_method_name
```


### Running Tests with Custom Format
To facilitate running tests and formatting the output, a custom script (test.py) has been created.
- This script uses unittest for executing tests and customizes the output format for readability.
- The script scans the tests directory for files matching test_*.py and runs all test cases.
- Test names are displayed in cyan color for clarity.

[//]: # (- Results are indicated with green check marks &#40;<span style="color:green;">✔</span>&#41; for success and red cross marks &#40;<span style="color:red;">✘</span>&#41; for failures.Output is structured to show each test name followed by its result for easy tracking of test progress and outcomes.)
- Results are indicated with emojis:
  - Green check mark (**✅**) for success
  - Red cross mark (**❌**) for failures.
- To run the tests, execute the following command:

```bash
python test.py
```
To add filtering for running a specific test using your custom test runner


```bash
python test.py tests.test_fib_payment_integration_service.TestFIBPaymentIntegrationService.test_create_payment_success
```

- Running test: test_get_token............ ✅
- Running test: test_check_payment_status_success............ ✅
- Running test: test_create_payment_success............ ✅
- Running test: test_refund_success............ ❌



---


### Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.


---


### License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.


---

### Support

For support, please contact support@fib-payment.com or visit our website.

---

### Acknowledgments

Thanks to the FIB Payment development team for their contributions. This SDK uses the `requests` library for API requests.

---

### Versioning

We use semantic versioning (SemVer) principles for subsequent releases (v0.2.0, v0.3.0, etc.). For the versions available, see the tags on this repository.

---

### FAQ

#### Q: How do I get an API key for the FIB Payment system?

A: Please contact our support team at support@fib-payment.com to request an API key.

#### Q: Can I use this SDK in a production environment?

A: Yes, the SDK is designed for use in production environments, but please ensure you have configured it correctly and have got the