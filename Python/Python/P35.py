class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        self.area = length*width
        self.perimeter = 2*(length+width)

    def __str__(self):
        return f"Length = {self.length}\nWidth = {self.width}\nArea = {self.area}\nPerimeter = {self.perimeter}"    

r1 = Rectangle(6,3)
print(r1)    