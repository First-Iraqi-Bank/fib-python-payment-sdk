# FIB Payment SDK

The FIB Payment SDK provides seamless integration with the FIB payment system, empowering developers to streamline payment transactions and facilitate secure refunds within their applications.

## Features

- **Payment Transactions**: Enable users to make payments securely through the FIB payment system, handling transactions effortlessly within your application.
- **Refund Processing**: Process refunds securely through the FIB payment system, managing transactions efficiently within your application.
- **Payment Status Checking**: Check the status of payments to ensure accurate transaction tracking.
- **Payment Cancellation**: Cancel payments securely through the FIB payment system, providing flexibility and control over payment transactions.

## Installation

To integrate the SDK into your project, install it via pip:

```bash
pip install fib-payment-sdk
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

### Usage of the SDK

Below is a basic example of how to use the SDK:

#### Ensure Dependencies are Installed:
Make sure you have installed all required dependencies using pip:
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables:
Create a `.env` file in the root directory of your project and configure the necessary environment variables. Refer to the `.env.example` file for the required variables.

#### Create a Payment Example Usage
To create a payment, use the `create_payment` method. This method will return the payment details which you can store in a database or cache for later use in other functionalities like callback URL handling, checking payment status, cancelling payment, and refunding payment.

```python
import os
from dotenv import load_dotenv
from fib_payment_sdk.services import FIBAuthIntegrationService, FIBPaymentIntegrationService

# Load environment variables from the .env file
load_dotenv()

# Initialize the authentication service
auth_service = FIBAuthIntegrationService()

# Initialize the payment integration service
payment_service = FIBPaymentIntegrationService(auth_service)

try:
    # Create a new payment
    payment_response = payment_service.create_payment(1000, 'http://localhost/callback', 'Test payment description')
    
    # Extract payment details from the response
    payment_data = payment_response.json()
    
    # Payment details (example using a dictionary)
    payment_details = {
        'fib_payment_id': payment_data['paymentId'],
        'readable_code': payment_data['readableCode'],
        'personal_app_link': payment_data['personalAppLink'],
        'valid_until': payment_data['validUntil'],
    }

    # #TODO: Store the payment details in a database or cache. These details will be used for other functionalities such as handling callback URLs, checking payment status, and canceling payments.
    # Return the payment details to the end user to proceed with the payment
    return payment_details
except Exception as e:
    print(f"Error: {e}")
```

- Storing Payment Details: Once you receive the payment details from the `create_payment` method, you can store them in a database or a cache.
  This allows you to retrieve and use these details for further actions such as checking the payment status, processing refunds, or handling payment callbacks.

    - Database: Save the payment details in a relational database (e.g., MySQL, PostgreSQL) or a NoSQL database (e.g., MongoDB).
    - Cache: Use an in-memory cache (e.g., Redis, Memcached) to store the payment details for quick access.

- Returning Payment Details: After storing the payment details, return them to the end user. The returned details include:

    - `fib_payment_id`: The unique identifier for the payment.
    - `readable_code`: A readable code for the payment.
    - `personal_app_link`: A link for the end user to proceed with the payment in the personal app.
    - `valid_until`: The expiration time for the payment.

By following these steps, you ensure that the payment details are securely stored and easily accessible for further processing.

#### Checking the Payment Status
To check the status of a payment, use the `check_payment_status` method. This method requires the `payment_id` which was returned when the payment was created.

```python
payment_status = payment_service.check_payment_status(payment_id)
print(f"Payment Status: {payment_status}")
```

#### Refunding a Payment
To refund a payment, use the `refund` method. This method also requires the `payment_id`.

```python
refund_response = payment_service.refund(payment_id)
```

#### Cancelling a Payment
To cancel a payment, use the `cancel` method. This method requires the `payment_id`.

```python
cancel_response = payment_service.cancel(payment_id)
```

#### Handling Payment Callbacks
To handle payment callbacks, ensure your application has a POST API or URL that FIB can call to notify your application about payment status updates.

Callback URL Requirements: Your callback URL should be able to handle POST requests with a request body containing two properties:

- `id`: This represents the payment ID associated with the callback.
- `status`: This indicates the current status of the payment. Refer to the "Check Payment Status" section of this documentation for more details. The status returned should mirror the data structure returned by the check status endpoint.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/callback', methods=['POST'])
def callback():
    payload = request.get_json()
    
    # Validate incoming payload
    payment_id = payload.get('id')
    status = payload.get('status')
    
    if not payment_id or not status:
        return jsonify({'error': 'Invalid callback payload'}), 400
    
    # Process the callback
    try:
        payment_service.handle_callback(payment_id, status)
        # TODO: Implement your callback handling logic here
        
        return jsonify({'message': 'Callback processed successfully'})
    except Exception as e:
        return jsonify({'error': f'Failed to process callback: {e}'}), 500
```

##### Notes
- Replace `/callback` with your actual endpoint URL.
- Ensure your callback endpoint is accessible to FIB and handles errors gracefully.
- Implement the `handle_callback` method in your `FIBPaymentIntegrationService` class to handle the payment status update internally.

### FIB Payment Documentation

For comprehensive details on FIB Online Payment, please refer to the [full documentation](https://documenter.getpostman.com/view/18377702/UVCB93tc).

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
- Results are indicated with green check marks (<span style="color:green;">✔</span>) for success and red cross marks (<span style="color:red;">✘</span>) for failures.Output is structured to show each test name followed by its result for easy tracking of test progress and outcomes.
- To run the tests, execute the following command:

```bash
python test.py
```
To add filtering for running a specific test using your custom test runner


```bash
python test.py tests.test_fib_payment_integration_service.TestFIBPaymentIntegrationService.test_create_payment_success
```

- Running test: test_get_token............ <span style="color:green;">✔</span>
- Running test: test_check_payment_status_success............ <span style="color:green;">✔</span>
- Running test: test_create_payment_success............ <span style="color:green;">✔</span>
- Running test: test_refund_success............ <span style="color:red;">✘</span>




### Contributing

Contributions are welcome! Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

### License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

### Support

For support, please contact support@fib-payment.com or visit our website.

### Acknowledgments

Thanks to the FIB Payment development team for their contributions. This SDK uses the `requests` library for API requests.

### Versioning

We use semantic versioning (SemVer) principles for subsequent releases (v0.2.0, v0.3.0, etc.). For the versions available, see the tags on this repository.

### FAQ

#### Q: How do I get an API key for the FIB Payment system?

A: Please contact our support team at support@fib-payment.com to request an API key.

#### Q: Can I use this SDK in a production environment?

A: Yes, the SDK is designed for use in production environments, but please ensure you have configured it correctly and have got the