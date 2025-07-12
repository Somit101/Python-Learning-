x=int(input(("enter first number")))
y=int(input(("enter second number")))
print("Sum", x + y)
print("Difference", x - y)
print("Product", x * y)

if y != 0:
    print("Division", x / y)
else:
    print("Not defined")   


#BMI
W = float(input("Enter your weight (Kg)"))
H = float(input("Enter your height (m)"))
G = H * H
print("Your BMI", W / G)
