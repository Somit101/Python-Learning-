class Students:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name}\nRoll number: {self.roll_no}\nMarks: {self.marks}"
    
    def check(self):
        if self.marks>= 40:
            print("Pass")
        else:
            print("Fail")    

s1 = Students("Somit","1",98)
print(s1)        
s1.check()