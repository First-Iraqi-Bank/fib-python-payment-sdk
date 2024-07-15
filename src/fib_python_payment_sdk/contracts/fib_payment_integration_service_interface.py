from abc import ABC, abstractmethod


class FIBPaymentIntegrationServiceInterface(ABC):

    @abstractmethod
    def create_payment(self, amount: int, callback, description):
        pass

    @abstractmethod
    def check_payment_status(self, payment_id):
        pass

    @abstractmethod
    def handle_callback(self, payment_id: str, status: str):
        pass

    @abstractmethod
    def refund(self, payment_id: str):
        pass

    @abstractmethod
    def cancel(self, payment_id: str):
        pass
