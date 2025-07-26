def Menu():
   print("\n<<< Menu >>>")
   print("1.Create account")
   print("2.Find account by account number")
   print("3.Transfer money")
   print("4.Show all accounts")
   print("5.Exit")


class BankAccount:

    next_account = 1001
    def __init__(self,account_name,balance = 0):
        self.account_name = account_name
        self.balance = balance
        self.account_number = BankAccount.next_account
        BankAccount.next_account += 1

        
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.balance += amount

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdraw amount")
            return
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def display_balance(self):
        print( f"Account balance: {self.balance}")
    
    

            
    def __str__(self):
        return f"Name = {self.account_name}\nAccount number = {self.account_number}\nBalance = {self.balance}"
    


class BankSystem:
    def __init__(self):
        self.accounts = []

    def create_account(self,info):
        self.accounts.append(info)
        
    def find_account(self,acc_no):
        found = False
        for user in self.accounts:
            if user.account_number == acc_no:
                print( f"Name: {user.account_name}\nBalance: {user.balance}")
                found = True
        if not found:
            print("Invalid account number")

    def get_acc(self,acc_no):
        for account in self.accounts:
            if account.account_number == acc_no:
                  return account
        return None      
        

    def transfer(self,from_acc,to_acc,amount):
         sender = self.get_acc(from_acc)
         receiver = self.get_acc(to_acc)

         if not sender or not receiver:
             print("Invalid account number")
             return
         if sender.balance < amount:
             print("Insufficient balance")
             return

         sender.withdraw(amount)
         receiver.deposit(amount)   
         print("Transaction complete")
         print(sender.display_balance() )         


bank = BankSystem()


while True:
    Menu()
    User_input = int(input("Enter your task (1 - 5): "))
    if User_input == 1:
        Name = str(input("Enter your name: "))
        initial = int(input("Initial deposit amount: "))
        A = BankAccount(Name,initial)
        bank.create_account(A)
    elif User_input == 2:
        acc_no = int(input("Enter your account number: "))
        bank.find_account(acc_no)
    elif User_input == 3:
        acc1 = int(input("Enter account number of sender: "))
        acc2 = int(input("Enter account number of receiver: "))
        amt = int(input("Enter amount you want to send: "))
        bank.transfer(acc1,acc2,amt)
    elif User_input == 4:
        for account in bank.accounts :
            print(account) 
    elif User_input == 5:
        print("Exit successfull")
        break          
    else:
        print("Invalid input")    
            

            
        