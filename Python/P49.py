# Vending machine
import sqlite3
class Item:
    def __init__(self,item1,item2,item3,item4):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4

    def __str__(self):
        return f"1. {self.item1}\n2. {self.item2}\n3. {self.item3}\n4. {self.item4}"

class Money:
    def __init__(self,m1,m2,m3,m4):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4

    def __str__(self):
        return f""
I = Item()

def add_item():
    admin1 = input("Enter first item: ")
    admin2 = input("Enter second item: ")
    admin3 = input("Enter third item: ")
    admin4 = input("Enter fourth item: ")

    I.item1 = admin1
    I.item2 = admin2
    I.item3 = admin3
    I.item4 = admin4

    conn = sqlite3.connect('item.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Items 
                 (Item1 TEXT,
                 Item2 TEXT,
                 Item3 TEXT,
                 Item4 TEXT)""")
    c.execute('''INSERT INTO Items VALUES (?,?,?,?)''',)




def admin_main():
    print("<<<<< Admin Interface >>>>>")
    print("1. Add item")
    print("2. Assign money")
    print("3. Exit")





def user_main():
    print("<<<<< Today's Menu >>>>>")
    print("")


def login():
    print("<<<<< Login Interface >>>>>")
    print("1. Admin")
    print