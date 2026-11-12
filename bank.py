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
    def withdraw(self, amount, balance):
        # Trying to take out more than what's available?
        if amount > balance:
            # If so, you'll see "Insufficient funds"
            raise ValueError("\033[91m *** Insufficient funds *** \033[0m")
        else:
            # shortcut for self.balance = self.balance - amount (This updates and overwirtes the stored balance inside the acccount [because of the equals sign])
            self.balance -= amount
            # success message
            return print(f"\033[92m${amount} successfully deposited!\033[0m")
    # This returns a string representation of the account and can be called when needed ==>>> print(__str__())
    def __str__(self):
        return f"Account #5555 Owner: {self.owner}, Balance: ${self.balance}"

# This is an object for Anna's bank, and it's made from the BankAccount class
class AnnaBank(BankAccount):
    # initializes the object and its contents as positional arguments (account number, owner, balance)
    def __init__(self, account_number, owner, balance):
        # This line tells Python to call the BankAccount's __init__
        super().__init__(account_number, balance)
        # These three lines set the variables as attributes of the object
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
# This uses the BankAccount blueprint
account = AnnaBank(555, "Anna", 50)
# Attempts to deposit an amount (inside parentheses)
try:
    account.deposit(40)
    print(f"\033[92mSuccessful deposit!\033[0m")
# If it fails, an error message gets printed
except ValueError as e:
    print(f"\033[91m{e}: Attempted to deposit -- *** Transaction failed ***\033[0m")

# Attempts to withdraw an amount from the account
try:
    account.withdraw(20, 80)
    print(f"\033[92mSuccessful withdrawl\033[0m")
# If the try check fails, this is the error message
except ValueError as e:
    print(f"\033[91mAttempted to withdraw: Transaction failed:{e}\033[0m")

# Prints the account info from the __str__() method
print(account.__str__())