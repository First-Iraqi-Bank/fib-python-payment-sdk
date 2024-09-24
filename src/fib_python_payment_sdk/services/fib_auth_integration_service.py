import time

import requests

from ..config.fib import config


def retry(callback):
    max_attempts = 3
    last_exception = None

    for attempt in range(max_attempts):
        try:
            return callback()
        except Exception as e:
            last_exception = e
            if attempt < max_attempts - 1:
                time.sleep(0.1)  # Delay before retrying

    # If all attempts fail, throw the last caught exception
    if last_exception is not None:
        raise last_exception
    else:
        raise Exception("Retry function failed without catching any exceptions.")


class FIBAuthIntegrationService:
    def __init__(self):
        self.config = config
        self.account = self.config['clients'][self.config['auth_account'] or 'default']

    def get_token(self):
        try:
            print(self.account['client_id'], self.account['secret'], self.config['grant'])
            response = retry(
                lambda: requests.post(self.config['login'], auth=(self.account['client_id'], self.account['secret']),
                                      data={'grant_type': self.config['grant']}))

            if response.status_code == 200 and 'access_token' in response.json():
                return response.json()['access_token']

            raise Exception('Failed to retrieve access token.')
        except Exception as e:
            raise e
