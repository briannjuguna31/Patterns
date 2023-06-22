"""
DIP:-> want a class to depend on ABSTRACTIONS and not concrete Sub-classes
the payment processors are depending on specific authorizers SMSAuth
change the dependency . now authorizer in __init__ expects  authorizer of type Autorizer (which could be any authorizer not just SMSAuth)
can have : SMSAuth authorizer, NotARobot authorizer
NOTE:SOLUTION:Use ABSTRACT CLASS
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

class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass

class SMSAuth(Authorizer):
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
    
class NotARobot(Authorizer):
    """ Has two methods
        ONE: for verifying the sms code
        TWO: for verifying that its authorized
    """
    authorized = False

    def not_a_robot(self):
        print("Are you a robot ? Naaa...")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):
    """Payment processor for debit card payments."""
    
    def __init__(self, security_code, authorizer:Authorizer):
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
    
    def __init__(self, email_address,authorizer: Authorizer):
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


# now you can  easily swap authorizers
order_2 = Order()
order_2.add_item("Keyboard", 1, 50)
order_2.add_item("SSD", 1, 150)
order_2.add_item("USB cable", 1, 150)

print("Order total:", order_2.total_price())
authorizer = NotARobot()
payment_processor = PaypalPaymentProcessor("brighton@company.com",authorizer)
authorizer.not_a_robot()
payment_processor.pay(order_2)
