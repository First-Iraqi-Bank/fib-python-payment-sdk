import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from src.fib_payments.client import FIBPaymentsClient
from src.fib_payments.config import FIBConfig
from src.fib_payments.exceptions import AuthenticationError, APIError


@pytest.fixture
def mock_http_client():
    return AsyncMock()


@pytest.fixture
def mock_config():
    config = MagicMock(spec=FIBConfig)
    config.client_id = 'test_client_id'
    config.client_secret = 'test_client_secret'
    config.api_url = 'https://api.example.com'
    config.currency = 'IQD'
    config.callback_url = 'https://callback.example.com'
    config.refundable_for = 3600
    return config


@pytest.fixture
async def client(mock_config, mock_http_client):
    with patch('src.fib_payments.client.HTTPClient', return_value=mock_http_client):
        client = FIBPaymentsClient(mock_config)
        yield client
        await client.close()


@pytest.mark.asyncio
async def test_get_token_success(client, mock_http_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'access_token': 'test_token'}
    mock_http_client.request.return_value = mock_response
    with patch.object(client, 'http_client', mock_http_client):
        token = await client._get_token()

    assert token == 'test_token'


@pytest.mark.asyncio
async def test_request_success(client, mock_http_client):
    client.token = 'test_token'
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'key': 'value'}
    mock_http_client.request.return_value = mock_response

    result = await client._request('GET', '/test')

    assert result == {'key': 'value'}
    mock_http_client.request.assert_called_once_with(
        'GET',
        f"{client.config.api_url}/test",
        headers={
            'Authorization': 'Bearer test_token',
            'Content-Type': 'application/json',
            'User-Agent': 'FIBPaymentsSDK',
        }
    )


@pytest.mark.asyncio
async def test_request_failure(client, mock_http_client):
    client.token = 'test_token'
    mock_response = AsyncMock()
    mock_response.status_code = 400
    mock_response.text = 'Bad Request'
    mock_http_client.request.return_value = mock_response

    with pytest.raises(APIError):
        await client._request('GET', '/test')


@pytest.mark.asyncio
async def test_create_payment(client):
    client._request = AsyncMock(return_value={'id': 'payment_id'})

    result = await client.create_payment(100.0, 'EUR', 'https://custom-callback.com', 'Test payment')

    assert result == {'id': 'payment_id'}
    client._request.assert_called_once_with(
        'POST',
        '/payments',
        json={
            'monetaryValue': {'amount': 100.0, 'currency': 'EUR'},
            'statusCallbackUrl': 'https://custom-callback.com',
            'description': 'Test payment',
            'refundableFor': client.config.refundable_for,
        }
    )


@pytest.mark.asyncio
async def test_get_payment_status(client):
    client._request = AsyncMock(return_value={'status': 'completed'})

    status = await client.get_payment_status('payment_id')

    assert status == 'completed'
    client._request.assert_called_once_with('GET', '/payments/payment_id/status')


@pytest.mark.asyncio
async def test_refund_payment(client):
    client._request = AsyncMock(return_value={'status': 'refunded'})

    result = await client.refund_payment('payment_id')

    assert result == {'status': 'refunded'}
    client._request.assert_called_once_with('POST', '/payments/payment_id/refund')


@pytest.mark.asyncio
async def test_cancel_payment(client):
    client._request = AsyncMock(return_value={'status': 'cancelled'})

    result = await client.cancel_payment('payment_id')

    assert result == {'status': 'cancelled'}
    client._request.assert_called_once_with('POST', '/payments/payment_id/cancel')


@pytest.mark.asyncio
async def test_context_manager(mock_config, mock_http_client):
    with patch('src.fib_payments.client.HTTPClient', return_value=mock_http_client):
        async with FIBPaymentsClient(mock_config) as client:
            assert isinstance(client, FIBPaymentsClient)
        mock_http_client.close.assert_called_once()


if __name__ == '__main__':
    pytest.main()