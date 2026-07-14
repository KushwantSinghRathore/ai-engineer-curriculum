from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  

class CreditCard(Payment):
    def process_payment(self, amount):
        print(f"Payment Done from CreditCard of Amount: {amount}.")

class UPI(Payment):
    def process_payment(self, amount):
        print(f"Payment Done from UPI of Amount: {amount}.")

# --- Test ---
my_pay = CreditCard()
my_pay.process_payment(500)