class Bankaccount:
    def __init__(self):
        self.account_number=input("enter the account number:")
        self.name=input("enter the name:")
        self.account_type=input("enter the account type:")
        self.balance=0
    def deposit(self):
        amount=int(input("enter the amount to be deposited:"))
        self.balance+=amount
    def withdraw(self):
        amount=int(input("enter the amount to be withdraw:"))
        if self.balance>amount:
            self.balance-=amount
            print("balance=",self.balance)
        else:
            print("withdraw not possible")
a=Bankaccount()
a.deposit()
a.withdraw()
        