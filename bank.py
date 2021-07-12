class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def withdrawal(self,amount):
        if(amount>self.balance):
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Your available balance is " +str(self.balance))

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Your available balance is " +str(self.balance))
b=BankAccount("Nirmai",10000)
print(b)
print(b.owner)
print(b.balance)
b.withdrawal(1000)
b.deposit(500)
b.withdrawal(3000)
b.deposit(2000)
b.withdrawal(1500)
b.deposit(2000)
b.withdrawal(9500)
