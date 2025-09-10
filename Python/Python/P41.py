class Citizen:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eligibility(self):
        if self.age >= 18:
            return f"{self.name} can vote"
        
    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}"

c1 = Citizen("Somit",19)      
print(c1)
print(c1.eligibility())

