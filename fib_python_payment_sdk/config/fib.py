from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Define configurations using environment variables
config = {
    'login': os.getenv('FIB_BASE_URL', '') + '/auth/realms/fib-online-shop/protocol/openid-connect/token',
    'base_url': os.getenv('FIB_BASE_URL', '') + '/protected/v1',
    'grant': os.getenv('FIB_GRANT_TYPE', 'client_credentials'),
    'refundable_for': os.getenv('FIB_REFUNDABLE_FOR', 'P7D'),
    'currency': os.getenv('FIB_CURRENCY', 'IQD'),
    'callback': os.getenv('FIB_CALLBACK_URL', ''),
    'auth_account': os.getenv('FIB_ACCOUNT', 'default'),
    'clients': {
        'default': {
            'client_id': os.getenv('FIB_CLIENT_ID', ''),
            'secret': os.getenv('FIB_CLIENT_SECRET', ''),
        },
    },
}

# Optionally, you can print the configuration for debugging purposes
if __name__ == "__main__":
    print(config)
