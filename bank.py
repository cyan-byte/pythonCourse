class BankAccount:
    # Here, "self" is the mandatory first parameter inside class methods. It points to the specific object being used
    # This is the setup function
    def __init__(self, account_number, owner, balance=0):
        # These are the attributes (the variables attached to self that store the object's data)
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    # This is the method with built-in error checking
    def deposit(self, amount):
        if amount < 0:
            # This raises an error inside the class if the amount is negative (< 0)
            raise ValueError("Deposit amount must be above zero to deposit.")
        # add the balance to the amount deposited
        self.balance += amount

    def withdraw(self, amount):
        # Trying to take out more than what's available?
        if amount > self.balance:
            # If so, you'll see "Insufficient funds"
            raise ValueError("\033[91m *** Insufficient funds *** \033[0m")
        # shortcut for self.balance = self.balance - amount (This updates and overwirtes the stored balance inside the acccount [because of the equals sign])
        self.balance -= amount
        # success message
        return print(f"\033[92m${amount} successfully withdrawn!\033[0m")

    # This returns a string representation of the account and can be called when needed ==>>> print(__str__())
    def __str__(self):
        return f"Account #{self.account_number} Owner: {self.owner}, Balance: ${self.balance}"


# This is an object for Anna's bank, and it's made from the BankAccount class
class AnnaBank(BankAccount):
    # initializes the object and its contents as positional arguments (account number, owner, balance)
    def __init__(self, account_number, owner, balance):
        # This line tells Python to call the BankAccount's __init__
        super().__init__(account_number, owner, balance)


# This uses the BankAccount blueprint
account = AnnaBank(5555, "Anna", 50)
# Attempts to deposit an amount (inside parentheses)
try:
    account.deposit(40)
    print(f"\033[92mSuccessful deposit!\033[0m")
# If it fails, an error message gets printed
except ValueError as e:
    print(f"\033[91m{e}: Attempted to deposit -- *** Transaction failed ***\033[0m")

# Attempts to withdraw an amount from the account
try:
    account.withdraw(20)
    print(f"\033[92mSuccessful withdrawl\033[0m")
# If the try check fails, this is the error message
except ValueError as e:
    print(f"\033[91mAttempted to withdraw: Transaction failed:{e}\033[0m")

# Prints the account info from the __str__() method
print(account.__str__())


# Savings Account Subclass (inheriting from BankAccount)
class SavingsAccount(BankAccount):
    # The initializer is modified to accept interest_rate and maintenance fee.
    def __init__(self, interest_rate, maintenance_fee, account_number="0000", owner="Anna", balance=900):
        # This pulls from the base class
        super().__init__(account_number, owner, balance)
        # These two lines set the variables as attributes of the object
        self.interest_rate = interest_rate
        self.maintenance_fee = maintenance_fee

    def __str__(self):
        return f"\033[93mAccount #{self.account_number}\033[0m Owner: {self.owner}; Balance: ${self.balance}; Interest Rate: {self.interest_rate}%; Maintenance Fee: ${self.maintenance_fee}"

    def apply_interest(self):
        return self.interest_rate * self.balance

account2 = SavingsAccount(.05, 0)
try:
    account2.deposit(-5)
    print(f"\033[92mSuccessfuly added to Savings Account!")
except ValueError as e:
    print(f"\033[91m{e}\033[0m")
try:
    account2.withdraw(80)
except ValueError as e:
    print(f"\033[91m{e}\033[0m")
print(account2.__str__())
print(f"Applied interest: ${account2.apply_interest()}")