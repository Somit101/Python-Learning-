# Flight management system
# 1.What are the things in my problem (Classes)
# 2.What does each thing know (Attributes)
# 3.What each thing do (Functions)
# 4.How do these things work together (Object interact with each other)

import sqlite3

# Ticket booking
class ticketbooking:
    new_prn = 10120
    seat = 1
    def __init__(self,name,email,phone,destination,food_status,boarding):
        self.id = ticketbooking.new_prn
        self.name= name
        self.email= email
        self.phone= phone
        self.destination= destination
        self.seat = ticketbooking.seat 
        self.food_status = food_status
        self.boarding = boarding
        ticketbooking.seat +=1
        ticketbooking.new_prn += 1

def __str__(self):
        return f"Name = {self.name}\nPNR = {self.pnr}\nSeat_no = {self.seat_no}\nFood status = {self.food_status}\nBoarding date = {self.boarding_date}\nBoarding time = {self.boarding_time}"        

class Functions:
    def __init__(self):
         self.details = []

    def add(self,a):
         self.details.append(a)     
         
    def luggage(self,name,seat_no):
            Sr_no = 1
            self.Sr_no = Functions.luggage.Sr_no
            self.name = name
            self.seat_no = seat_no
            Functions.luggage.Sr_no += 1

    def Food_booking(self,starter,sweet,drink,main_course):
         self.starter = starter
         self.sweet = sweet
         self.drink = drink
         self.main_course = main_course
         
function = Functions()

def admin_interface():
     print("\n***Admin Interface***")
     print("1.Flight details")
     print("2.Food details")
     
     User_input = int(input("Enter what you want to do (1,2): "))
     if User_input == 1:
          Number = int(input("Enter filght number: "))
          name = str(input("Enter name of pilot: "))
          boarding_date = str(input("Enter boarding date (dd/mm/yyyy): "))
          boarding_time = str(input("Enter boarding time (hh:mm): "))
          boarding = str(input("Enter the place from where flight will take off: "))
          destination = str(input("Enter destination: "))
          conn = sqlite3.connect("Admin.db")
          
          c = conn.cursor()
          c.execute("""CREATE TABLE IF NOT EXISTS flight(\"Flight number\" INTEGER,\"Pilot name\" TEXT,\"Boarding Date\"TEXT,\"Boarding Time\" TEXT,\"Take off place\" TEXT,\"Destination\" TEXT)""")
          c.execute(f"INSERT INTO flight VALUES('{Number}','{name}','{boarding_date}','{boarding_time}','{boarding}','{destination}')")
          conn.commit()
          conn.close()
          print("Flight added successfully")


     elif User_input == 2:
          sql = sqlite3.connect("Food.db")
          s=sql.cursor()
          s.execute("""CREATE TABLE IF NOT EXISTS food(\"Drink\" TEXT,\"Starter\" TEXT,\"Sweet\" TEXT,\"Main Course\" TEXT)""")
          for i in range (3):
               drinks = input(f"Enter name of drink {i+1}: ")
               starter = input(f"Enter starter {i+1}: ")
               sweet = input(f"Enter sweet {i+1}: ")
               main = input(f"Enter main course {i+1}: ")
               s.execute(f"INSERT INTO food VALUES('{drinks}','{starter}','{sweet}','{main}')")
     
          sql.commit()
          sql.close()
          print("Food details added successfully")     

     else:
          print("Invalid input please enter correct values")

def User_interface():
     print("\n***User Interface***")
     print("1.Book tickets")
     print("2.My details")
     print("3.Food")
     print("4.Flight details")
     print("5.All flights")

     User_input = int(input("What do you want to do (1,2,3,4): "))
     if User_input == 1:
          name = str(input("Enter name of passanger: "))
          email = str(input("Enter valid email id: "))
          phone = int(input("Enter valid phone number: "))
          Destination = str(input("Enter destination: "))
          food_status = str(input("Enter if food taken or not(Yes/No): "))
          boarding = str(input("Enter the place from where you want to board the flight: "))

          use2 = sqlite3.connect("user.db")
          u2 = use2.cursor()
          u2.execute("""CREATE TABLE IF NOT EXISTS user1(\"Name\" TEXT,\"Email\" TEXT,\"Phone no\" INTEGER,\"Destination\" TEXT,\"Food\" TEXT,\"Boarding\" TEXT)""")
          u2.execute(f"INSERT INTO user1 VALUES('{name}','{email}','{phone}','{Destination}','{food_status}','{boarding}')")
          use2.commit()
          use2.close()

          use = sqlite3.connect("Admin.db")
          u = use.cursor()
          u.execute(f"SELECT 'Boarding date' FROM flight WHERE 'Take off place' = '{boarding}' AND Destination = '{Destination}'") 
          u.execute(f"SELECT 'Boarding time' FROM flight WHERE 'Take off place' = '{boarding}' AND Destination = '{Destination}'")
          use.commit()
          use.close()
          assign = ticketbooking(name,email,phone,Destination,food_status,boarding)
          function.add(assign)

     elif User_input == 2:
          phone1 = int(input("Enter your phone number: "))
          use1 =  sqlite3.connect("user.db")
          u1 = use1.cursor()
          h = u1.execute(f"""SELECT * FROM user1 WHERE "Phone no" = '{phone1}'""")  
          H = h.fetchall()
          print("[Name, Email, Phone no, Destination, Food, Boarding]")
          for i in H:
               print(i)
          use1.commit()
          use1.close()

     elif User_input == 3:                                            ########################################
          hi = sqlite3.connect("Food.db")
          K = hi.cursor()
          Food = K.execute("""SELECT * FROM food""")
          Go = Food.fetchall()
          print("\n******* All Food Details *******")
          print("[Drink, Starter, Sweet, Main Course]\n")
          count = 0
          for i in Go:
               if count <= 3:
                 print(f"{count + 1}. {i}")
                 count += 1

          user = int(input("Enter 1,2,3: "))

          


          hi.commit()                                
          hi.close()     
               

     elif User_input == 4:
          fnum = int(input("Enter flight number: "))
          fdate = input("Enter date of boarding (dd/mm/yyyy): ")
          Flight = sqlite3.connect("Admin.db")
          Fl = Flight.cursor()
          F = Fl.execute(f"""SELECT * FROM flight WHERE "Flight number" = '{fnum}' AND "Boarding Date" = '{fdate}'""")
          Fly = F.fetchall()
          print("\n--------- Flight Details ---------")
          for i in Fly:
               print(i)                              

     elif User_input == 5:
          board = str(input("Enter boarding place: "))
          drop = str(input("Enter destination: "))
          All = sqlite3.connect("Admin.db")
          Al = All.cursor()
          A = Al.execute(f"""SELECT * FROM flight WHERE "Take off place" = '{board}' AND "Destination" = '{drop}'""")      
          Allfly = A.fetchall()
          for i in Allfly:  
            print(i)    

def main():
     print("\n<<<<<<<<<< Welcome to flight booking >>>>>>>>>>")
     print("1. Admin")
     print("2. User")
     print("3. Exit")

while True:
     main()
     User = int(input("Enter 1,2,3: "))
     if User == 1:
          admin_interface()

     elif User == 2:
          User_interface()

     elif User == 3:
          print("Exit successfull")  
          break          
     else:
          print("Plese enter valid inputs")





           

          
          
          
          
          
          
     


        
