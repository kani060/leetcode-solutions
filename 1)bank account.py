# # 1. Bank Account — Encapsulation Concept: Encapsulation Create a BankAccount class with accountNumber, holderName and balance. Requirements: • Balance must not be directly modifiable from outside the class. • Implement deposit() and withdraw(). • Withdrawal must fail when the balance is insufficient. • 
# Do not allow negative deposit or withdrawal amounts. • Create objects and perform multiple transactions.

class BankAccount:

    def __init__(self, accountNumber, holderName, balance):
        self.accountNumber = accountNumber
        self.holderName = holderName
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.__balance += amount
            print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("Withdrawn:", amount)

    def getBalance(self):
        return self.__balance

account1 = BankAccount("101", "Kanisgha", 5000)
account1.deposit(2000)
account1.withdraw(1000)
account1.withdraw(7000)
print("Current Balance:", account1.getBalance())
