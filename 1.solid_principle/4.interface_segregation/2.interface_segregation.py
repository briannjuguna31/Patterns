"""
    class PaymentProcessor(ABC):
        def __init__(self, security_code):
            self.security_code = security_code

        @abstractmethod
        def auth_sms(self, order):
            pass

        @abstractmethod
        def pay(self, order):
            pass
            
There is an issue with defining a generic interface like
having the PaymentProcessor to do multiple things
Things that are not always applicable to SUBCLASSES
NOTE:EXAMPLE: its only DEBIT & PAYPAL subclasses that do (sms authorization)
NOTE:SOLUTION: CREATE SEPERATE INTERFACE FOR THIS(sms varification)
A second sub-class of PaymentProcessor that adds  sms 2FA
NOTE:IN-SUMMARY: Instead of one general purpose interface , we split it 
so that sub-classes can have meaningful behaviors
"""
from abc import ABC, abstractmethod

class Order:
    """Handles adding items to the order and calculating the total price."""
    
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        """Adds an item to the order.

        Args:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
            price (float): The price of the item.
        """
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        """Calculates the total price of the order.

        Returns:
            float: The total price.
        """
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class PaymentProcessor(ABC):
    """Abstract base class for payment processors."""
    
    def __init__(self, security_code):
        self.security_code = security_code

    @abstractmethod
    def pay(self, order):
        pass
class PaymentProcessor_SMS(PaymentProcessor):
    """Abstract base class for payment processors."""
    @abstractmethod
    def auth_sms(self, order):
        pass

   
class DebitPaymentProcessor(PaymentProcessor_SMS):
    """Payment processor for debit card payments."""
    
    def __init__(self, security_code):
        super(PaymentProcessor).__init__(security_code)
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    """Payment processor for credit card payments."""
    
    def __init__(self, security_code):
        super(PaymentProcessor).__init__(security_code)

    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor_SMS):
    """Payment processor for PayPal payments."""
    
    def __init__(self, email_address):
        super(PaymentProcessor).__init__()
        self.email_address = email_address
        self.verified = False

    def auth_sms(self, code):
        print(f"Verifying SMS code: {code}")
        self.verified = True

    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 1, 150)

print("Order total:", order.total_price())

payment_processor = PaypalPaymentProcessor("brighton@company.com")
payment_processor.auth_sms(12345)
payment_processor.pay(order)
