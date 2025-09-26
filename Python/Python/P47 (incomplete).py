def menu():
    print("\n<<< School Students Manager >>>")
    print("1.Add student")
    print("2.Display all students")
    print("3.Find by roll number")
    print("4.Save student data")
    print("5.Load student data")
    print("6.Exit")

class Student:
    def __init__(self,name,roll_no,Class,dict):
        self.name = name
        self.roll_no = roll_no
        self.Class = Class
        self.dict = dict

    def total(self,name):
        if name == self.name:
            print(sum(self.dict.values()))

    def __str__(self):
        return f"Name: {self.name}, Roll no.: {self.roll_no}, Class: {self.Class}, Marks: {self.dict}"        



class ResultSystem:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def display_all(self):
        if not self.students:
            print("No data available")
        else: 
           for student in self.students:   
              print(student)

    def find_by_roll(self,Roll_no):
        found = False
        for student in self.students:
            if student.roll_no == Roll_no:
                print(student)
                found = True
        if not found:
                print("Recheck student Roll number")

    def save(self):
        if not self.students:
            print("Please first add student")
        else:    
         added = False
         for student in self.students:
          with open("School data.txt","r") as data:
            if student.name in data.read():
                print(f"{student} already exists")
                added = True
         if not added:
                with open ("School data.txt","a") as append:  
                  append.write(f"{student}\n")

    def load(self,name):
        try:
            with open("School data.txt","r") as look:
                if name in look.read():
                    print(look.readline())

        except:  
            print("Student not found")  

result = ResultSystem() 

while True:
    menu()
    try:
        User_input = int(input("Enter (1,2,3,4,5,6): "))
    except:
        print("Please enter integers only")
    else:
        if User_input == 1:
            try:

                  Name = str(input("Enter name of student: ")).capitalize()
                  Roll_no = int(input("Enter roll number of student: "))
                  Class = int(input("Enter class of student: "))
                  Marks_in_maths = int(input("Enter marks obtained in Mathematics(100): "))
                  Marks_in_Science = int(input("Enter marks obtained in Science(100): "))  
                  Marks_in_english = int(input("Enter marks obtained in English(100): ")) 

            except:
                print("Please enter proper integers and name")
            else:
                student = {}
                student.update({"Mathematics":Marks_in_maths,"Science":Marks_in_Science,"English":Marks_in_english})  
                
                Output = Student(Name,Roll_no,Class,student)      
                result.add_student(Output)  
                print(f"{Name} added successfully")   

        elif User_input == 2:
            result.display_all()

        elif User_input == 3:
            try:
                roll = int(input("Enter roll number of student: "))

            except:
                print("Please enter valid integers")
            else:
                result.find_by_roll(roll)  

        elif User_input == 4:
            with open("School data.txt","a") :
              result.save()

        elif User_input == 5:
            try:
              name = str(input("Enter name to student: "))
            except:
                print("Please write a valid name")
            else:
                result.load(name)      
            

        elif User_input == 6:
            print("Exit successfull")
            break

        else:
            print("Please enter valid integers")        
            

           






        













