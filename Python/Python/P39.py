class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        Area = self.radius * self.radius
        return f"Area: {Area}"

    def circumference(self):
        Circumference = (self.radius + self.radius) * 3.14
        
        return f"Circumference: {Circumference}"

    def __str__(self):
        return f"Radius: {self.radius}"

Radius = int(input("Enter radius: "))
C1 = Circle(Radius)  
print(C1)    
print(C1.area())
print(C1.circumference())
