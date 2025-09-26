# Vending machine

class Item:
    def __init__(self,item1,price1,item2,price2,item3,price3,item4,price4):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        self.price1 = price1
        self.price2 = price2
        self.price3 = price3
        self.price4 = price4


    def __str__(self):
        return f"1. {self.item1} : {self.price1}\n2. {self.item2} : {self.price2}\n3. {self.item3} : {self.price3}\n4. {self.item4} : {self.price4}"
    
    

class Money:
    def __init__(self):
       self.items = []
       self.money = []


    def add(self,l1,m1):
       self.items.append(l1)  
       self.money.append(m1) 

    
M = Money()

def add_item_and_money():
    admin1 = input("Enter item 1: ")
    price1 = input("Enter price of item 1: ")
    admin2 = input("Enter item 2: ")
    price2 = input("Enter price of item 2: ")
    admin3 = input("Enter item 3: ")
    price3 = input("Enter price of item 3: ")
    admin4 = input("Enter item 4: ")
    price4 = input("Enter price of item 4: ")

    I = Item(admin1,price1,admin2,price2,admin3,price3,admin4,price4)
    M.add(admin1,price1)
    M.add(admin2,price2)
    M.add(admin3,price3)
    M.add(admin4,price4)
    


def admin_main():
    print("\n<<<<< Admin Interface >>>>>")
    print("1. Add item")
    try:
      user = int(input("Enter 1 or 2: "))
    except:
       print("Put valid inputs only")
    else:
       if user == 1:
          add_item_and_money()
       else:
          print("No options available")
                

def user_main():
    print("\n<<<<< Today's Menu >>>>>")
    print(f"1. {M.self.items[0]} : {M.self.money[0]}")
    print(f"2. {M.self.items[1]} : {M.self.money[1]}")
    print(f"3. {M.self.items[2]} : {M.self.money[2]}")
    print(f"4. {M.self.items[3]} : {M.self.money[3]}")

    try:
       user = int(input("Enter 1,2,3,4: "))
    except:
       print("Put valid integers only")
    else:
             
       if user == 1:
          print(f"Total amount: {M.self.money[0]}")
       elif user == 2:
          print(f"Total amount: {M.self.money[1]}")  
       elif user == 3:
          print(f"Total amount: {M.self.money[2]}")    
       elif user == 4:
          print(f"Total amount: {M.self.money[3]}")  
       else:
          print("Invalid input")    
       

def login():
    print("\n<<<<< Login Interface >>>>>")
    print("1. Admin")
    print("2. User")
    try:
       user = int(input("Enter 1 or 2: "))
    except: 
        print("Put valid inputs only")
    else:       
      if user == 1:
        admin_main()
      elif user == 2:
        user_main()           
      else:
        print("")        

while True:
    login()
