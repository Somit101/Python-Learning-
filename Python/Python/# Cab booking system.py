# Cab booking system

class Details:
    def __init__(self,name,age,phone_no,email,num_of_vehicle,vehicle_type,age_of_vehicle):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.email = email
        self.num_of_vehicle = num_of_vehicle
        self.vehicle_type = vehicle_type
        self.age_of_vehicle = age_of_vehicle

    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}\nPhone = {self.phone}\nEmail = {self.email}"
    
class Driver:
    def __init__(self):
        self.drivers = []

    def add(self,driver):
        if self.drivers == []:
            print("No driver exists")
        else:    
           self.drivers.append(driver)    

    def remove(self,name,phone):
        found = False
        for driver in self.drivers:
            
            if driver.name == name and driver.phone_no == phone:
                self.drivers.pop(driver)
                found = True
        if not found:
            print("No driver exists of this name")

    def change_status(self,status):
        for driver in self.drivers:
            driver.status =  status

    def view(self,phone):
        found = False
        for driver in self.drivers:
            
            if driver.phone_no == phone  :
                print(driver)
                found = True      
        if not found:
            print("No driver with this phone number exists")

# I need to write the same things as i wrote in driver class make a function which can be used in both the classes so no duplication happens
class Rider:
    def __init__(self):
        self.riders = []

    def add(self,rider):
        if self.riders == []:
            print("No rider exists")
        else:    
           self.riders.append(rider)   

    def remove(self,name,phone):
        found = False
        for rider in self.riders:
            
            if rider.name == name and rider.phone_no == phone:
                self.riders.pop(rider)
                found = True
        if not found:
            print("No rider exists of this name")

    def view(self,phone):
        found = False
        for rider in self.riders:
            
            if rider.phone_no == phone:
                print(rider)
                found = True      
        if not found:
            print("No rider with this phone number exists")                                                                   

    

def main():
    print("\n------------ Main Menu ------------")
    print("1.Admin interface")
    print("2.Driver interface")
    print("3.Rider interface")
    print("4.Exit")

def admin():
    print("\n<<<<<<< Admin interface >>>>>>>") 
    print("1.Remove driver")   
    print("2.View driver")
    print("3.Remove user")
    print("4.View user")
    print("5.Return to Main interface")

def driver():
    print("\n<<<<<<<<< Driver Interface >>>>>>>>>")
    print("1.Add yourself")
    print("2.Change status")
    print("3.Return to Main interface")

def rider():
    print("\n<<<<<<<<< Rider Interface >>>>>>>>>")  
    print("1.Add yourself")
    print("2.Drop location")
    print("3.Pick up location")
    print("4.Return to Main interface")

    
D = Driver()
R = Rider()


while True:
    main()
    try: 
       User_input = int(input("Enter 1,2,3,4: "))
    except:
        print("Enter valid numbers only")
    else:
        if User_input == 1:
            admin()
            try: 
               user = int(input("Enter 1,2,3,4,5,6: "))
            except:
                print("Please enter valid integers")
            else:

                if user == 1:
                    Name = str(input("Enter name of driver you want to remove: "))
                    Phone = int(input("Enter the phone number of driver you want to remove: "))
                    D.remove(Name,Phone) 

                elif user == 2:
                    phone_no = int(input("Enter phone number of driver: "))
                    D.view(phone_no)          

                elif user == 3:
                    Name1 = str(input("Enter name of user you want to remove: "))
                    Phone1 = int(input("Enter phone number of user you want to remove: "))
                    R.remove(Name1,Phone1)

                elif user ==  4:
                    Phone_no = int(input("Enter phone number of user you want to view: "))
                    R.view(Phone_no)

                elif user == 5:
                    main()    

                else:
                    print("Envalid input")    


        elif User_input == 2:
            driver()
            try:
               User = int(input("Enter 1,2: "))
            except:
                print("Please inter valif inputs only")
            else:       
              if User == 1:
                    name = str(input("Enter your name: "))
                    age = int(input("enter your age: "))
                    phone = int(input("Enter your phone number: "))
                    email = str(input("Enter your email: "))
                    vehicle_no = str(input("Enter vehicle number\nlike: MH 37 AD 1234:"))
                    vehicle_type = str(input("Enter type of vehicle: "))
                    age_of_vehicle = int(input("Enter age of vehicle: "))

                    D.add(name,age,phone,email,vehicle_no,vehicle_type,age_of_vehicle)

              elif User == 2:           ##########
                  Status = str(input("Enter your status 'Available' or 'Not Available': "))

              elif User == 3:
                  main()    

            # status 
        elif User_input == 3:
            rider()
            try:
              user_input = int(input("Enter 1,2,3: "))
            except:
                print("Please inter valid inputs only")
            else:

                if user_input == 1:
                    name1 = str(input("Enter your name: "))
                    age1 = int(input("enter your age: "))
                    phone1 = int(input("Enter your phone number: "))
                    email1 = str(input("Enter your email: "))

                    R.add(name1,age1,phone1,email1)

                elif user_input == 2:                        #########
                    drop = str(input("Enter drop location: "))
                    pick = str(input("Enter pick up location: "))    
                    print(f"Driver will pick y;ou up from {pick} and drop you to {drop}")

                elif user_input == 3:
                    main()    

        elif User_input == 4:
            print("Exit successfull")
            break

        else:
            print("Invalid input")      



        




