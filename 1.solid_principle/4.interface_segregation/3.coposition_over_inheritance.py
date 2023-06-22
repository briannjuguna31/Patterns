"""
If you support sms_verification(2FA), then inherit form this class
NOTE: We want to use COMPOSITION Instead of INHERITANCE(more sub-classes)
NOTE:SOUTION:Create a seperate class that handles the authentication
NOTE:bcs in most cases you don't need big inheritance trees
Just need to seperate the different kinds of behaviour in your app(composition works just fine)
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

class SMSAuth:
    """ Has two methods
        ONE: for verifying the sms code
        TWO: for verifying that its authorized
    """
    authorized = False

    def verify_code(self,code):
        print(f"verifying code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized 



   
class DebitPaymentProcessor(PaymentProcessor):
    """Payment processor for debit card payments."""
    
    def __init__(self, security_code, authorizer:SMSAuth):
        super(PaymentProcessor).__init__(security_code)
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
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

class PaypalPaymentProcessor(PaymentProcessor):
    """Payment processor for PayPal payments."""
    
    def __init__(self, email_address,authorizer: SMSAuth):
        super(PaymentProcessor).__init__()
        self.email_address = email_address
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 1, 150)

print("Order total:", order.total_price())
authorizer = SMSAuth()
payment_processor = PaypalPaymentProcessor("brighton@company.com",authorizer)
authorizer.verify_code(23455)
payment_processor.pay(order)
