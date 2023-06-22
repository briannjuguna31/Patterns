"""Cohesion has been increased bcz the classes have single responsibility
    but we introduces some coupling (Dependency): Payment processor depends on order
    Returns:
        _type_: _description_
"""
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
        



class PaymentProcessor:
    """Handle payment processing
        no longer need to know the payment type (its encoded in the method name)
    """
    def pay_debit(self,order,security_code):
        """Acknowledge the payment_type and set order status to PAID

        NOTE: now coupling/dependency has been itroduced (Payment processor func depends on order)
        it needs the order to update its STATUS
        Args:
            security_code (_type_): _description_
        """
        print("Processing debit payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self,order,security_code):
        print("Processing debit payment type")
        print(f"verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard",1,50)
order.add_item("SSD",1,150)
order.add_item("USB cable",1,150)

print("Order total",order.total_price())
payment_processor = PaymentProcessor()
payment_processor.pay_credit(order,"037566")
