#method level
#  method is intended for internal use within the class and not to be accessed directly from external code.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self._validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount):
        self._validate_amount(amount)
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount.")
        

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._engine_status = 'off'

    def start_engine(self):
        self._perform_engine_checks()
        self._engine_status = 'on'

    def stop_engine(self):
        self._engine_status = 'off'

    def get_engine_status(self):
        return self._engine_status

    def _perform_engine_checks(self):
        # Perform complex engine checks
        print("Performing engine checks...")

class KCB(BankAccount):
    pass

kcb = KCB("MCB", 100)
kcb.deposit(-500)
