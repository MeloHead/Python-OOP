class User:
    def __init__(self,f_name,l_name):
        self.first_name=f_name
        self.last_name=l_name
        self.balance = 0


    def make_deposit(self,amount):
        self.balance+=amount
        return self

    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
        
    def display_user_balance(self):
        print(self.first_name,self.last_name, self.balance)
        return self

user1=User("matt","R")
user1.make_deposit(50).make_deposit(100).make_deposit(150).make_withdrawal(100).display_user_balance()

user2 = User("nicky","chaurasia")
user2.make_deposit(101).make_deposit(101).make_withdrawal(100).make_withdrawal(100).display_user_balance()


user3 = User("vic","geeeeee")
user3.make_deposit(301).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()