class bankAccount:
    def __init__(self,balance):
        self.balance = balance


    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def transfer(self,to,amount):
        if self.balance>=amount:
            self.balance-=amount
            to.balance+=amount
        else:
            print("Your balance is",self.balance)



account1 = bankAccount(100)
account2 = bankAccount(200)

account1.transfer(account2, 50)

print(account1.balance)
print(account2.balance)