class User:
    def __init__(self,f_name,l_name):
        self.first_name=f_name
        self.last_name=l_name
        self.account = BankAccount()
        

    def make_deposit(self,amount):
        self.account.balance+=amount
        return self

    def make_withdrawal(self, amount):
        self.account.balance-=amount
        return self

    def display_user_balance(self):
        print(self.first_name,self.last_name, self.account.balance)
        return self


class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

account1 = User("Vic","G")
account1.make_deposit(50).make_withdrawal(25).display_user_balance()
