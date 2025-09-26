# [(date,amount,category,type,not),(date,amount,category,type,note)]
import datetime
import sqlite3

class Transaction:
    def __init__(self,date,amount,category,type,note):
        self.date = date
        self.amount = amount
        self.category = category
        self.type = type
        self.note = note

    def __str__(self):
        return f"Category = {self.category}\nDate = {self.date}\nAmount = {self.amount}\nType = {self.type}\nNote = {self.note}"

class FinanceTracker:
    def __init__(self):
        self.sources = []

    def __init__db(self):
        # Creating table if not exist
        conn = sqlite3.connect("self.db_name")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXIST finance (Id INTEGER PRIMARY KEY AUTOINCREMENT,Category TEXT,Date TEXT, Amount INTEGER, Type TEXT, Note TEXT)")

        conn.commit()
        conn.close()


    def add_transaction(self,Source):
        self.sources.append(Source)
        
    def show_summary(self):
        Income = []
        Expense = []
        for source in self.sources:

            if source.type == "Income":
              Income.append(source.amount)
            elif source.type == "Expense":
                Expense.append(source.amount)
            else:
                print("The finance tracker is empty")
        I = sum(Income)
        J = sum(Expense)
        print(f"Total Income = {I}")
        print(f"Total Expenses = {J}")
        print(f"Total balance = {I-J}")

    def show_by_category(self,name):
        Income = []
        Expense = []
        for source in self.sources:
            if source.type == "Income" and source.category == name:
                Income.append(source.amount)
            elif source.type == "Expense" and source.category == name:
                Expense.append(source.amount)   
        I = sum(Income)
        J = sum(Expense)
        print(f"Total for {name}: {I-J}")         
            

    def search_by_date(self,date):
        found = False
        for source in self.sources:
            if source.date == date:
                print(f"{source}\n")
    
            found = True
        if not found:
            print("Given date does not match to any option")         

    def save_to_file(self):
        conn = sqlite3.connect("Finance.db")
        c = conn.cursor()
        for source in self.sources:
           c.execute("INSERT INTO finance(Category,date,amount,type,note) VALUES(?,?,?,?,?)"),
           (source.category,source.date,source.amount,source.type,source.note)

        conn.commit()
        conn.close()
        self.sources.clear()
        print("Data saved successfully")

    #def load_from_file():


finance = FinanceTracker()
 

def main():
    print("\n<<<<<< Personal Finance Tracker >>>>>>")
    print("1.Add income")
    print("2.Add expense")
    print("3.Show summary")
    print("4.Show by category")
    print("5.Search by date")
    print("6.Save to file")
    print("7.Load from file")
    print("8.Exit")

while True:
    main()
    try:
        User_input = int(input("Welcome Sir what would you like to do today (1,2,3,4,5,6,7,8): "))
    except:
        print("Please enter given integers only")    
    else:
        if User_input == 1:
            try:
                
                date = str(input("Enter date (dd/mm/yyyy): "))
                amount = int(input("Enter amount: "))
                category = (input("Enter category: ")).capitalize()
                Type = str(input("Type (income/expense): ")).capitalize()    
                note = input("Enter any note for future: ")
    
            except:
                print("Please write correct expressions")
            else: 
                Assign = Transaction(date,amount,category,Type,note)
      
                finance.add_transaction(Assign)

        elif User_input == 2:
            try:
                date = str(input("Enter date (dd/mm/yyyy): "))
                amount = int(input("Enter amount: "))
                category = (input("Enter category: ")).capitalize()
                Type = str(input("Type (income/expense): ")).capitalize()
                note = input("Enter any note for future: ")
            except:
                print("Please write correct expressions")
            else: 
                B = Transaction(date,amount,category,Type,note)
      
                finance.add_transaction(B)

        elif User_input == 3:
            (finance.show_summary())

        elif User_input == 4:
                Category = input("Enter the category you want to review: ").capitalize()
                finance.show_by_category(Category)


        elif User_input == 5:
            date = str(input("Enter date of event(dd/mm/yyyy): "))
            finance.search_by_date(date) 
        elif User_input ==6:
            finance.pysave_to_file()    
        elif User_input == 8:
            print("The finance tracker will be waiting for you the next time\nExit successfull")
            break       

        else:
            print("Invalid input please enter given integers only")    

                





