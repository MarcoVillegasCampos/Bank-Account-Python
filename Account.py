class Account:
    bankName="Coding Dojo Bank"
    allBankAccounts=[]

    def __init__(self, InterestRate,  ):
        self.interestRate=InterestRate       
        self.balance= 0.0
       

    def withdraw (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
           
            print(f"Insuficient funds:Chargin a $5 fee.")
            self.withdraw(5)
        return self

    def deposit (self, amount):
        self.balance+= amount
        return self

    def displayAccountInfo(self):
        print(f"Account balance: {self.balance}.")
        return self
    def transferMoney (self, amount, account):
        if amount >= self.balance:
            print("We cannot process your transfer.")
            print(f"The origin account has: {self.balance}.")
            print(f"And you are trying to transfer{amount}.")
        else:
            self.balance -= amount
            account.balance += amount
        return self
    def yield_interest(self):
        interest=self.balance * self.interestRate
        self.balance += interest
        return self

    @classmethod
    def printAllAccountInfo (cls):
        for account in cls.allBankAccounts:
            account.printInfo()
        

  