mydict = {}

def menu():
     print("\nMenu")
     print("1. Add contact")
     print("2. Search contact (name)")
     print("3. Search contact (number)")
     print("4. Delete contact")
     print("5. Update contact")
     print("6. Exit")

def add_contact():
     name = str(input("Enter name of candidate : ")).capitalize()
     if name in mydict:
          print("Contact already exist")
     else:    
          
          number = int(input("Enter contact number : "))
          mydict.update({name:number})
          print(name,"Added successfully") 
     
     
def search_contact():
     search = str(input("Enter name of candidate : ")).capitalize()
     if search in mydict:
          print(search,":",mydict[search])
     else:
          print("Name not found")     
    
                   
def delete_contact():
     delete = str(input("Enter name of candidate : ")).capitalize()
     if delete in mydict:
          mydict.pop(delete) 
          print(delete,"deleted")   
     else:
          print("Name not found") 

def update_contact():
     G = str(input("Enter name of candidate : ")).capitalize()
     if G in mydict:
          N = int(input("Enter new contact number : "))
          mydict.update({G:N})
     else:
          print("Name not available")     
          

def search_contacts():
     contact = int(input("Enter contact number : "))
     for x,y in mydict.items():
          if y == contact :
               print(x,":",y)
          else:
               print("Not found")         
           

     

while True:
     menu()
     Input = input("What do you want to perform(1,2,3,4,5,6)? : ")
     if Input == "1":
          add_contact()
     elif Input == "2":
          search_contact()
     elif Input == "3":
          search_contacts()
     elif Input == "4":
          delete_contact()
     elif Input == "5":
          update_contact()
     elif Input == "6":
          print("Thank you!!!")

          break
     else:
          print("Invalid task")               
                