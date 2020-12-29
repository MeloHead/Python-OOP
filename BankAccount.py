class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("yield interest: $" + str(self.int_rate))
        print("your balance is: " + str(self.balance))
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(3).deposit(3).deposit(5).withdraw(1).yield_interest().display_account_info()
account2.deposit(21).deposit(30).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()

#little iffy on how yield_interest() works... review later