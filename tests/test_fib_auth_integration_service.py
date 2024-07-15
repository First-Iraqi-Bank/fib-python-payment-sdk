import unittest
from unittest.mock import patch, MagicMock
from fib_python_payment_sdk.services.fib_auth_integration_service import FIBAuthIntegrationService


class TestFIBAuthIntegrationService(unittest.TestCase):

    def setUp(self):
        self.service = FIBAuthIntegrationService()

    @patch('requests.post')
    def test_get_token(self, mock_post):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'access_token': 'test_token'}
        mock_post.return_value = mock_response

        # Act
        result = self.service.get_token()

        # Assert
        self.assertEqual(result, 'test_token')
        mock_post.assert_called_once()

    # Add more tests as needed


if __name__ == '__main__':
    unittest.main()
