# Flight management system
# 1.What are the things in my problem (Classes)
# 2.What does each thing know (Attributes)
# 3.What each thing do (Functions)
# 4.How do these things work together (Object interact with each other)
import sqlite3

# Ticket booking
def ticketbooking():
    new_prn = 10120
    seat = 1
    def __init__(self,name,email,phone,destination,food_status,boarding_date,boarding_time,boarding):
        self.id = ticketbooking.new_prn
        self.name= Name
        self.email= Email   `1  l
          00+63.3
        +-
        self.phone= Phone
        self.destination= Destination
        self.seat = TicketBooking.seat 
        self.food_status = Food_status
        self.boarding_date = boarding_date
        self.boarding_time = boarding_time
        self.boarding = boarding
        TicketBooking.seat +=1
        TicketBooking.new_PNR += 1

def Functions():
    def __init__(self):
         self 
         
         

    def luggage(self,name,seat_no):
            Sr_no = 1
            self.Sr_no = luggage.Sr_no
            self.name = name
            self.seat_no = seat_no
            luggage.Sr_no += 1

    def Food_booking(self,starter,sweet,drink,main_course):
         self.starter = starter
         self.sweet = sweet
         self.drink = drink
         self.main_course = main_course
         
                 

def Passan3ger_details():
    def __init__(self,name,PNR,seat_no,food_status,boarding_date,boarding_time,Destination):
        self.name= name
        self.pnr = PNR
        self.seat_no = seat_no
        self.food_status = food_status
        self.boarding_date = boarding_date
        self.boarding_time = boarding_time
        self.destination = Destination

    def __str__(self):
        return f"Name = {self.name}\nPNR = {self.pnr}\nSeat_no = {self.seat_no}\nFood status = {self.food_status}\nBoarding date = {self.boarding_date}\nBoarding time = {self.boarding_time}"  

Ticket_booking = TicketBooking()
Function = Functions()
def admin_interface(self):
     print("***Admin Interface***")
     print("1.Flight details")
     print("2.Food details")
     
     User_input = int(input("Enter what you want to do (1,2,): "))
     if User_input == 1:
          Number = int(input("Enter filght number: "))
          name = str(input("Enter name of pilot: "))
          boarding_date = str(input("Enter boarding date (dd/mm/yyyy): "))
          boarding_time = str(input("Enter boarding time (hh:mm): "))
          boarding = str(input("Enter the place from where flight will take off: "))
          destination = str(input("Enter destination: "))
          conn = sqlite3.connect("Admin.db")
          
          c = conn.cursor()
          c.execute("CREATE TABLE IF NOT EXISTS flight(Flight number INTEGER,Pilot name TEXT,Boarding Date TEXT,Boarding Time TEXT,Take off place TEXT,Destination TEXT)")
          c.execute(f"INSERT INTO flight VALUES({Number},{name},{boarding_date},{boarding_time},{boarding},{destination}")
          conn.commit()
          conn.close()
          print("Flight added successfully")

     elif User_input == 2:
          sql = sqlite3.connect("Food.db")
          s=sql.cursor()
          s.execute("CREATE TABLE IF NOT EXIST food(Drink TEXT,Starter TEXT,Sweet TEXT,Main Course TEXT)")
          for i in range (3):
               drinks = input(f"Enter name of drink {i+1}: ")

               starter = input(f"Enter starter {i+1}: ")

               sweet = input(f"Enter sweet {i+1}: ")

               main = input(f"Enter main course {i+1}: ")

               s.execute(f"INSERT INTO food VALUES({drinks},{starter},{sweet},{main})")

          sql.commit()
          sql.close()     

     else:
          print("Invalid input please enter correct values")

def User_interface(self):
     print("***User Interface***")
     print("1.Book tickets")
     print("2.My details")
     print("3.Food")
     print("4.Flight details")

     User_input = int(input("What do you want to do (1,2,3,4): "))
     if User_input == 1:
          name = str(input("Enter name of passanger: "))
          email = str(input("Enter valid email id: "))
          phone = int(input("Enter valid phone number: "))
          Destination = str(input("Enter destination: "))
          food_status = str(input("Enter (Yes/No): "))
          boarding = str(input("Enter the place from where you want to board the flight: "))

          use = sqlite3.connect("Admin.db")
          u = use.cursor()
          H = u.execute(f"SELECT Boarding date FROM flight WHERE 'Take off place' = {boarding} AND Destination = {Destination}") 
          I = u.execute(f"SELECT Boarding time FROM flight WHERE 'Take off place' = {boarding} AND Destination = {Destination}")
          assign = TicketBooking(name,email,phone,Destination,food_status,H,I,boarding)

           

          
          
          
          
          
          
     


        
