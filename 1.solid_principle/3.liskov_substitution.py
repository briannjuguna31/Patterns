
""" 3. Liskov substitution
    If you have objects in a program,
    You should be able to replace those objects with instances of their(SUb-types)
    Without altering the correctness of the program

    Paypal payment s do not work with {security_codes}
    Instead they use email addresses

    You could change that by passing emails on class instanciation
    But that would abuse the {security_code dependancy} in the pay method in (PaymentProcessor)
    NOTE:SOLUTION: move the variable to the PaymentProcessor __init__ so its {DYNAMIC },
    THen change its name 
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
        """Process the payment for the order.

        Args:
            order (Order): The order to be paid.
        """
        pass

class DebitPaymentProcessor(PaymentProcessor):
    """Payment processor for debit card payments."""
    
    def __init__(self, security_code):
        super(PaymentProcessor).__init__(security_code)

    def pay(self, order):
        """Process the debit card payment for the order.

        Args:
            order (Order): The order to be paid.
        """
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):
    """Payment processor for credit card payments."""
    
    def __init__(self, security_code):
        super(PaymentProcessor).__init__(security_code)

    def pay(self, order):
        """Process the credit card payment for the order.

        Args:
            order (Order): The order to be paid.
        """
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):
    """Payment processor for PayPal payments."""
    
    def __init__(self, email_address):
        super(PaymentProcessor).__init__()
        self.email_address = email_address

    def pay(self, order):
        """Process the PayPal payment for the order.

        Args:
            order (Order): The order to be paid.
        """
        print("Processing PayPal payment type")
        print(f"Verifying email: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 1, 150)

print("Order total:", order.total_price())

payment_processor = PaypalPaymentProcessor("brighton@company.com")
payment_processor.pay(order)
