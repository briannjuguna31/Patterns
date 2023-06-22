"""2.Open/CLosed
Write code open for EXTENSION(
we should be able to extend the existing code   with new Functionality
) 
But closed for MODIFICATION(
	Don't need to modify the existing code in order to get there 
)
NOTE:QUESTION: Want to add new/extra payment method like (bitcoin,paypal) 
have to modify the payment processor class (this violates the OPEN/CLOSED principle)
NOTE:SOLUTION: Create a  structure of classes and sub-classes
Then define  new sub-classes for each payment type
NOTE:REFACTOR: PaymentProcessor to an abstract class , 
then individual payment types sub class it
base clas to have the basic bihaviour
"""

from abc import ABC, abstractmethod


class Order:
    """Handles adding staff to the order

    Returns:
        _type_: _description_
    """
    items = []
    quantities = []
    prices = []
    status = "open"



    def add_item(self,name,quantity,price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
        



class PaymentProcessor(ABC):
    """Handle payment processing
        no longer need to know the payment type (its encoded in the method name)
    """
    @abstractmethod
    def pay(self,order,security_code):
        pass

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing debit payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing credit payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing paypal payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard",1,50)
order.add_item("SSD",1,150)
order.add_item("USB cable",1,150)

print("Order total",order.total_price())
payment_processor = PaypalPaymentProcessor()
payment_processor.pay(order,"037566")
