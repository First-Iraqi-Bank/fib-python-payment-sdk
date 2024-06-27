import os

import requests
import time
import logging
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
        self.logger = logging.getLogger('fib')
        log_file_path = '../logs/fib.log'
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

        self.logger.addHandler(logging.FileHandler('../logs/fib.log'))
        self.logger.setLevel(logging.ERROR)

    def get_token(self):
        try:
            response = retry(
                lambda: requests.post(self.config['login'], auth=(self.account['client_id'], self.account['secret']),
                                      data={'grant_type': self.config['grant']}))

            if response.status_code == 200 and 'access_token' in response.json():
                return response.json()['access_token']

            self.logger.error('Failed to retrieve access token from FIB Payment API.', {'response': response.text})
            raise Exception('Failed to retrieve access token.')
        except Exception as e:
            self.logger.error('Error occurred while retrieving access token from FIB Payment API.',
                              {'message': str(e), 'trace': e.__traceback__})
            raise e
