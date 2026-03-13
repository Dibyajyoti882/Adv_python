class InsufficientBalance(Exception):
    pass


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise InsufficientBalance("Not enough balance")

            self.balance -= amount
            print("Withdrawal successful")

        except InsufficientBalance as e:
            print(e)

    def show_balance(self):
        print("Balance:", self.balance)


a = BankAccount("Dibyajyoti", 5000)

a.deposit(1000)
a.withdraw(2000)
a.withdraw(10000)
a.show_balance()