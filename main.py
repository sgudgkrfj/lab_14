class BancAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, balan):
        self.balance += balan
        print(f"Додали гроші")
    def withdraw(self, balan):
        self.balance -= balan
        print(f"Відняли гроші")

banc = BancAccount(123, 1000)
banc.deposit(10)
print(banc.balance)
banc.withdraw(100)
print(banc.balance)