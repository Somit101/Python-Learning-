H = int(input("Enter first number: "))
I = int(input("Enter second number: "))
operator = input("Enter the operator (+,-,*,/,**,//,%): ")
match operator:
    
    case "+":
        print(H+I)
    case "-":
        print(H-I)
    case "*":
        print(H*I) 
    case "/" if I!=0 :
        print(H/I)
    case "**":
        print(H**I)
    case "//":
        print(H//I)
    case "%":
        print(H%I)            

    case _:
        print("Wrong operator")               