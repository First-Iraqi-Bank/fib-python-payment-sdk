import json
import time

import requests

from .fib_auth_integration_service import FIBAuthIntegrationService
from ..config.fib import config
from ..contracts.fib_payment_integration_service_interface import FIBPaymentIntegrationServiceInterface


class FIBPaymentIntegrationService(FIBPaymentIntegrationServiceInterface):
    def __init__(self, fib_auth_integration_service: FIBAuthIntegrationService):
        self.fib_auth_integration_service = fib_auth_integration_service
        self.config = config
        self.base_url = self.config['base_url']
        self.max_attempts = 3
        self.retry_delay = 0.1  # seconds

    def request(self, method, url, data=None):
        token = self.fib_auth_integration_service.get_token()

        for attempt in range(self.max_attempts):
            try:
                headers = {
                    'Authorization': 'Bearer ' + token,
                    'Content-Type': 'application/json',
                }

                if method == 'POST':
                    response = requests.post(url, headers=headers, json=data)
                else:
                    response = requests.get(url, headers=headers)

                if response.status_code in [200, 201]:
                    return response.json()

                time.sleep(self.retry_delay)  # Delay before retrying
            except requests.exceptions.RequestException as e:
                print(
                    f"Failed to {method} request to FIB Payment API. URL: {url},"
                    f" Data: {json.dumps(data)}, Error: {str(e)}")
                raise Exception(f"Failed to {method} request due to: {str(e)}")

        print(f"Failed to {method} request after {self.max_attempts} attempts. URL: {url}, Data: {json.dumps(data)}")
        return None

    def get_request(self, url):
        return self.request('GET', url)

    def post_request(self, url, data=None):
        return self.request('POST', url, data)

    def create_payment(self, amount, callback=None, description=None):
        data = self.get_payment_data(amount, callback, description)
        return self.post_request(f"{self.base_url}/payments", data)

    def check_payment_status(self, payment_id):
        return self.get_request(f"{self.base_url}/payments/{payment_id}/status")['status']

    def handle_callback(self, payment_id, status):
        pass  # TODO: handle the callback implementation

    def get_payment_data(self, amount, callback=None, description=None):
        return {
            'monetaryValue': {
                'amount': amount,
                'currency': self.config['currency'],
            },
            'statusCallbackUrl': callback or self.config['callback'],
            'description': description or '',
            'refundableFor': self.config['refundable_for'],
        }

    def refund(self, payment_id):
        return self.post_request(f"{self.base_url}/payments/{payment_id}/refund")

    def cancel(self, payment_id):
        return self.post_request(f"{self.base_url}/payments/{payment_id}/cancel")
