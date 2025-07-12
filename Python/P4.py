H = str(input("Enter Username")).lower()

j = int(input("Enter password"))

if H == "admin" and j == 1234 :
    print("Login successful")
else:
    print("Invalid credentials")    



G = int(input("Enter first number"))
K = int(input("Enter second number"))
B = (input("Enter operator(+,-,*,/)"))

if B == "+" :
    print(G + K)
elif B == "-" :
    print(G - K)
elif B == "*":
    print(G * K)
elif B == "/":
    if K != 0:
        print(G / K)
    else :
        print("Invalid")         
else:
    print("Invalid operator")             





