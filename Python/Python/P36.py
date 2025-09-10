class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.add = num1+num2
        self.subtract = num1-num2
        self.multiply = num1*num2
        
    def divide(self):
        if self.num2!=0:
            self.divid = self.num1 / self.num2
            return f"Division: {self.divid}"

        else:
            print("Invalid")    

    def __str__(self):
        return f"Addition: {self.add}\nSubtraction: {self.subtract}\nMultiplication: {self.multiply}"

c1 = Calculator(3,6)
            
print(c1)
print(c1.divide())
        

