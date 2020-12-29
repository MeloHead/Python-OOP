class User:
    def __init__(self,f_name,l_name):
        self.first_name=f_name
        self.last_name=l_name
        self.balance = 0

    def make_deposit(self,amount):
        self.balance+=amount

    def make_withdrawal(self, amount):
        self.balance-=amount

    def display_user_balance(self):
        print(self.first_name,self.last_name, self.balance)

user1=User("matt","R")
user1.make_deposit(50)
user1.make_deposit(100)
user1.make_deposit(150)
user1.make_withdrawal(100)
user1.display_user_balance()

user2 = User("nicky","C")
user2.make_deposit(101)
user2.make_deposit(101)
user2.make_withdrawal(100)
user2.make_withdrawal(100)
user2.display_user_balance()

user3 = User("vic","G")
user3.make_deposit(301)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.make_withdrawal(100)
user3.display_user_balance()