class bank_account:
    def __init__(self):
        self.accno=int(input("enter the account number:"))
        self.name=input("enter the name:")
        self.account_type=input("enter account type:")
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        try:
            if(self.balance<amount):
                print("insufficent balance")
            else:
                self.balance=self.balance-amount
                return self.balance
        except:
            print("something went wrong")
obj1=bank_account()
amount1=int(input("enter the amount deposit:"))
print("account balance after deposit",obj1.deposit(amount1))
amount2=int(input("enter the amount to be withdraw:"))
print("account balance after withdrawel:",obj1.withdraw(amount2))
