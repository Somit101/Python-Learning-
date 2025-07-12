print("Dashboard\n")
print("1.Create Account")
print("2.Login")
Input = input("Create account(1) or login(2): ")

def create():
    username = input("Enter new username: ")
    
    with open("storage.txt","r") as see:
       
       if username in see.read().split():  
           print("Username already taken")
       else:
           password = input("Create a strong password including #,*,+,?: ")
           if "#" and "+" and "*" and "?" in password :
               with open("storage.txt","a") as create:
                  create.write(f"{username} : {password}\n")
               print("Account created successfully")   
           else:
               print("Create password including #,*,+,?")   
                   


def login():
    user = input("Enter your username: ")
    lock = input("Enter your password: ")
    
    with open("storage.txt","r") as look:
        line_to_check = f"{user} : {lock}"
        if line_to_check in look.read().splitlines():
            print("Login successfull")
        else:
            print("Invalid username or password")                    
              
if Input == "1":
    create()
elif Input =="2":
    login()    
else:
    print("Invalid task to perform")
                