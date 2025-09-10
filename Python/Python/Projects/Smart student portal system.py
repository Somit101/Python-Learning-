def menu():
  print("\n")
  print("Dashboard :")
  print("1.Add student")
  print("2.View whole school data")
  print("3.View class 10 data")
  print("4.View class 9 data")
  print("5.View class 8 data")
  print("6.Search student")
  print("7.Students with good attendence")
  print("8.Exit")
  global v
  v = input("Enter the task you want to perform (1,2,3,4,5,6,7,8): ")
               



def Login():
    with open("Users.txt","a") as save:
      save.write("")
    Input = input("Login or Register: ").lower()
    if Input == "register":
       user = input("Create a username: ")
       pas = input("Create a strong password: ")
       
       with open("Users.txt","r") as store:
           users = f"{user}:"
           if users in store.read().split():
              print("Username already exist")
           else:
                with open("Users.txt","a") as form:
                  form.write(f"{user}: {pas}\n")
       Login()  
              

    elif Input == "login":
       username = input("Enter your username: ")
       password = input("Enter your password: ")
       with open("Users.txt","r") as see:
          look = f"{username}: {password}"
          if look in see.read().splitlines():
            print("Login successfull")
            
          else:
            print("Invalid username or password")  
            Login()
    else:
       print("Invalid task to perform") 
       Login()                             
Login()


student = {}
def add():
   Data = {}
   global Name
   global Roll_no
   global Class
   Name = str(input("Enter name of student: ")).capitalize()
   Roll_no = (input("Enter roll no of student: "))
   Maths = int(input("Enter marks in mathematics (out of 100): "))
   Phy = int(input("Enter marks in physics (out of 100): "))
   Chem = int(input("Enter marks in chemistry (out of 100): "))
   Eng = int(input("Enter marks in english (out of 100): "))
   CS = int(input("Enter marks in computer science (out of 100): "))
   DOB = (input("Enter date of birth (dd/mm/yyyy): "))
   Gender = input("Enter gender: ").capitalize()
   Class = input("Enter class: ")
   Attendence = int(input("Enter attendence percentage: "))
   Percentage = (Maths+Phy+Chem+Eng+CS)/5
   student.update({"Name":Name,"Class":Class,"D.O.B":DOB,"Gender":Gender,"Mathematics":Maths,"Physics":Phy,"Chemistry":Chem,"English":Eng,"Computer Science":CS,"Attendence":Attendence,"Percentage":Percentage})

   Data.update({Roll_no:student})
   with open("Students.txt","a") as demo:
      demo.write("")


   global sort
   sort =f"(Name: {Name}),"
   global Sort   
   Sort = f"{Name}),"
   global Roll
   Roll = f"{Roll_no}:"
   if Class == "8":
         def class_8():
            
            
            with open("Class8.txt","a") as eight:
              eight.write("")
              
            with open("Class8.txt","r") as eighth:
              exists8 = False
              for line in eighth:
                 
               if sort in line or Roll in line:
                 exists8 =True
              if not exists8:
                 with open("Class8.txt","a") as eight_class:
                   eight_class.write(f"{Roll_no}: -> ")   
                   for a,b in student.items():
                     if a != "Percentage":
                       save8 = f"({a}: {b}), "
                       eight_class.write(save8)
                     else:
                          output = f"({a}: {b})\n" 
                          eight_class.write(output)
         class_8()
         
              
   elif Class == "9":        
       def class_9():    
      
        with open("Class9.txt","a") as nineth:
         nineth.write("")
         with open("Class9.txt","r") as nine:
            exists9 = False
            for line in nine:
               
              if sort in line or Roll in line:
               exists9 = True
               break  
            if not exists9:
               with open("Class9.txt","a") as nineth_class:
                 nineth_class.write(f"{Roll_no}: -> ")   
                 for c,d in student.items():
                    if c != "Percentage":
                       save9 = f"({c}: {d}), "
                       nineth_class.write(save9)
                    else:
                          output = f"({c}: {d})\n" 
                          nineth_class.write(output)    
       class_9()

         
   elif Class == "10": 
       def class_10():
          with open("Class10.txt","a") as tenth:
           tenth.write("")
           with open("Class10.txt","r") as ten:
              exists10 = False
              for i in ten:
                if sort in i or Roll in i:
                          exists10 = True
                          break          
              if not exists10:
                  with open("Class10.txt","a") as tenth_class:
                    tenth_class.write(f"{Roll_no}: -> ")   
                    for e,f in student.items():
                       if e != "Percentage":
                         save10 = f"({e}: {f}), "
                         tenth_class.write(save10)
                       else:
                          output = f"({e}: {f})\n" 
                          tenth_class.write(output)
       class_10()   
  
   # Storing data in Students.txt            
   clas = f"(Class: {Class})," 
     
   already_exists = False
   with open("Students.txt","r") as who:
    for line in who:
      if (sort in line and clas in line) or Roll in line :
              already_exists = True
              break
    if not already_exists:
        with open("Students.txt","a") as store:
             store.write(f"{Roll_no}: -> ")
             for key,value in student.items():
               if key != "Percentage":
                  line = f"({key}: {value}), "
                  store.write(line)
               else:
                  output = f"({key}: {value})\n" 
                  store.write(output) 

   with open("Students.txt","a") as f:
      f.write("")                

   # Attendence
   with open("Students.txt","r") as good:
     actual = False
     for i in good:
        
        sort = f"(Name: {Name}),"
        clas = f"(Class: {Class}),"
        if sort and clas in i:
           actual = True
           break
     if not actual and Attendence >= 75:
            a = f"({sort}{clas})\n"
            with open("Attendence_good","a") as mark:
                mark.write(a)                   
   
  
def view():
   with open("Students.txt","r") as view:
      print(view.read())


def Search_student():
   Search = input("Enter Name of student: ").capitalize()
   with open("Students.txt","r") as single:
      actual = f"{Search}),"
      for line_number,line in enumerate(single,1):
         if actual in line.split():
            print(line)
            


while True:
   menu()
   if v == "1":
     add()
   elif v == "2":
     view()
   elif v == "3":
             #class_10()
             with open("Class10.txt","r") as t:
               print(t.read())
             
   elif v == "4":
           #class_9()
           with open("Class9.txt","r") as n:
             print(n.read())
            
   elif v == "5":
            #class_8()
            with open("Class8.txt","r") as data8:
               print(data8.read())
   elif v == "6":
     Search_student()
   elif v == "7":
     with open("Attendence_good","r") as me:
        print(me.read())
   elif v == "8":
     print("Exit successfull")      
     break
   else:
     print("Invalid task to perform")
 
   
                        