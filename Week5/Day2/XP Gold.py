class BankAccount:
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def authenticate(self, username, password):
        if username == self.username and password == self.password:
            self.authenticated = True
            print(self.authenticated)
        else:
            self.authenticated = False
            print(self.authenticated)

    def deposit(self, amount):
        while self.authenticated:
            self.balance += amount
            return self.balance

    def withdraw(self, amount):
        while self.authenticated:
            self.balance -= amount
            return self.balance


class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance, username, password, minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance > self.minimum_balance:
            self.balance -= amount
            return self.balance
        else:
            print("not possible")


my_account = MinimumBalanceAccount(10000, "esso", 1234)
my_account.authenticate("ivi", 345123)
my_account.deposit(50000)
my_account.withdraw(15000)
print(my_account.balance)
