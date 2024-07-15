import unittest
from unittest.mock import patch, MagicMock
from src.fib_python_payment_sdk.services.fib_payment_integration_service import FIBPaymentIntegrationService
from src.fib_python_payment_sdk.services.fib_auth_integration_service import FIBAuthIntegrationService


class TestFIBPaymentIntegrationService(unittest.TestCase):
    def setUp(self):
        self.mock_auth_service = MagicMock(spec=FIBAuthIntegrationService)
        self.mock_auth_service.get_token.return_value = 'dummy_token'
        self.fib_payment_integration_service = FIBPaymentIntegrationService(self.mock_auth_service)

    @patch.object(FIBPaymentIntegrationService, 'post_request')
    def test_create_payment_success(self, mock_post_request):
        # Mock the return value of post_request
        mock_post_request.return_value = {'status': 'success'}

        response = self.fib_payment_integration_service.create_payment(100)
        self.assertEqual(response, {'status': 'success'})

    @patch.object(FIBPaymentIntegrationService, 'get_request')
    def test_check_payment_status_success(self, mock_get_request):
        # Mock the return value of get_request
        mock_get_request.return_value = {'status': 'success'}

        response = self.fib_payment_integration_service.check_payment_status('payment_id')
        self.assertEqual(response, 'success')

    @patch.object(FIBPaymentIntegrationService, 'post_request')
    def test_refund_success(self, mock_post_request):
        # Mock the return value of post_request
        mock_post_request.return_value = {'status': 'success'}

        response = self.fib_payment_integration_service.refund('payment_id')
        self.assertEqual(response, {'status': 'success'})


if __name__ == '__main__':
    unittest.main()

