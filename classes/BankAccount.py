# Write a class named BankAccount where each object remembers information about 
# a user's account at a bank. You must include the following public members:

# BankAccount(name): constructor - constructs a new account for the person with
# the given name, with $0.00 balance

# ba.name: property - the account name as a string (read - only)

# ba.balance: property - the account balance as a real number (read - only)

# ba.deposit(amount): method - adds the given amount of money, as a real number,
# to the account balance; if the amount is negative, does nothing

# ba.withdraw(amount): method - subtracts the given amount of money, as a real
# number, from the account balance; if the amount is negative or exceeds the 
# account's balance, does nothing

# You should define the entire class including the class heading, the private 
# instance variables, and the declarations and definitions of all the public 
# member functions and constructor.

class BankAccount:
    name: str
    balance: float

    def __init__ (self, name: str):
        self.name = name
        self.balance = 0.0
    
    def deposit (self, amount: float) -> None:
        if amount > 0:
            self.balance += amount

    def withdraw (self, amount: float) -> None:
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
