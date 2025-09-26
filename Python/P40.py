class Bank:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account = account_number
        self.balance = balance

    def deposit(self):
        depo = float(input("Enter the amount you want to deposit: "))
        amount = self.balance + depo
        return f"Balance: {amount}"
    
    def withdraw(self):
        withd = float(input("Enter the amount you want to withdraw: "))
        amount = self.balance - withd
        return f"Balance: {amount}"
    
    def __str__(self):
        return f"Name: {self.name}\nAccount number: {self.account}"
    
B1 = Bank("Somit","147258369",8000)
print(B1)
Input = input("Press 1 to deposit or Press 2 to withdraw: ")

if Input == "1":
    print(B1.deposit()   )
elif Input =="2":
    print(B1.withdraw())
else:
    print("Invalid")         
