

class BankAccount():
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.deposit_amt = 0
        self.withdraw_amt = 0
        
    
    def depo(self,amount):
        self.deposit_amt += amount
        self.balance += amount

    def withd(self,amount) :
        if self.balance >= amount:
            self.withdraw_amt += amount
            self.balance -= amount
        else:
            print("Insufficient balance")    
    
    def __str__(self):
        return f"Name: {self.name}\nAccount number: {self.account_number}\nDeposit amount: {self.deposit_amt}\nWithdraw amount: {self.withdraw_amt}\nBalance: {self.balance}"

class Details:
    def __init__(self,Name,Account_number,balance):
        self.name = Name
        self.account = Account_number
        self.bala = balance

    def __str__(self):
        return f"Name: {self.name}\nAccount number: {self.account}\nBalance: {self.bala}"
    
    def balan(self,bal):
        self.bala = bal


Input = int(input("Press 1 to withdraw/deposit or Press 2 to show account details: "))
if Input == 1:  
    Name = input("Enter name: ")
    Account = input("Enter account number: ")
    Bal = int(input("Enter account balance: "))
    withdraw = int(input("Enter withdrawal amount: "))
    deposit = int(input("Enter deposition amount: "))   
    f1 = BankAccount(Account,Name,Bal)
    f1.depo(deposit)
    f1.withd(withdraw)
    print(f1)   
elif Input == 2:
    Name = input("Enter name: ")
    Account = input("Enter account number: ")
    Bal = int(input("Enter account balance: "))
    f2 = Details(Name,Account,Bal)
    
    print(f2)



else:
    print("Invalid")     



