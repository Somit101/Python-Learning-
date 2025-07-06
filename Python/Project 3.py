#School management system
Dict = {"1":['Somit', 19, '28/02/2006', 10],"2":['Harsh',20,'30/03/2006',10]}

def menu():
    print("\nSchool menu")
    print("1.View all students data")
    print("2.Add new student")
    print("3.Remove student")
    print("4.Edit student data")
    print("5.Exit")

def view_data():
    print("Name, Age, DOB, Class")
    for i in Dict:
        print(i,":",Dict[i])
       
            

def add_student():
    G = int(input("Enter student number: "))
    H = input("Enter name of student: ")
    I = int(input("Enter age of student: "))
    J = input("Enter DOB of student (DD/MM/YYYY): ")
    K = int(input("Enter class of student: ")) 
    new_student = [] 
    new_student.append(H)
    new_student.append(I)
    new_student.append(J)
    new_student.append(K)
    Dict.update({G:new_student})
    print("Student added successfully")

def remove_student():
    Input = input("Enter student id: ")
    if Input in Dict:
        Dict.pop(Input)
        print("Student removed successfully")

def edit():
    num = input("Enter student id: ")
    if num in Dict:
        edited_values = []
        x = input("Enter name of student: ")
        c = input("Enter age of student: ")
        v = input("Enter DOB of student (DD/MM/YYYY): ")
        b = int(input("Enter class of student: "))
        edited_values.append(x)
        edited_values.append(c)
        edited_values.append(v)
        edited_values.append(b)
        Dict.update({num:edited_values})

        print("Completed")

while True:
    menu()
    M = input("Enter the task you want to perform (1,2,3,4,5): ")
    if M == "1":
        view_data()
    elif M == "2":
        add_student()
    elif M =="3":
        remove_student()
    elif M == "4":
        edit()
    elif M == "5":
        print("Thank you!!!")
        break
    else:
        print("Invalid task to perform")                






       
        




    



    






