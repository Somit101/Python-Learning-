Marks = {}
name = input("Enter name of student: ")
roll = input("Enter roll number: ")
sci = int(input("Marks in science: "))
maths = int(input("Marks in mathematics: "))
eng = int(input("Marks in english: "))
Marks.update({"Science":sci,"Mathematics":maths,"English":eng})

class Student:
                   
    
    def __init__(self,name,roll,marks):
        self.name = name 
        self.roll = roll 
        self.marks = marks 
        self.percent = sum(Marks.values())/len(marks)

    def get_grade(self):
            if self.percent>= 90:
              print("Grade: A")
            elif self.percent >= 80:
              print("Grade: B")
            elif self.percent >= 70:
              print("Grade: C")
            elif self.percent >= 60:
               print("Grade: D")
            elif self.percent >=50:
               print("Grade: E")
            elif self.percent >=40:
                print("Grade: F")   
            else:
               print("Fail")

        
    def __str__(self):
        return f"Name:{self.name}\nRoll no:{self.roll}\nMarks:{self.marks}\nPercentage:{self.percent:.2f}%" 

s1 = Student(name,roll,Marks)
print(s1)
s1.get_grade()