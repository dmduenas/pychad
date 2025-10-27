class BankAccount:
    min_balance = 100

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s new balance is {self._balance}")
        else:
            print("Deposit must be positive")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5

user1 = BankAccount("Alice", 500)
user1.deposit(700)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))