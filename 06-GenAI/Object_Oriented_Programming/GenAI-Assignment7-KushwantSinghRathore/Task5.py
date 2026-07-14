from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass  

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid {amount} using UPI.")


p1 = CreditCardPayment()
p1.process_payment(500)

p2 = UPIPayment()
p2.process_payment(300)