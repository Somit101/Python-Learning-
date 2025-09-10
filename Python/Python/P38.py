class Temperature:
    def __init__(self,temp):
        self.temp = temp

    def fahrenheit(self):
        Feh = self.temp*(9/5)+32
        return f"{Feh:.2f}deg fahrenheit"

    def __str__(self):
        return f"{self.temp}deg celsius is equal to = "

Input = float(input("Enter temperature in celsius: ")  )  
T1 = Temperature(Input)
print(T1)    
print(T1.fahrenheit())



