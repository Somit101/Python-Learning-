# Input
element_1 = int(input("Enter first number: "))
element_2 = int(input("Enter second number: ")) 
operator = input("Enter operator (+,-,/,*): ")
list_elements = [element_1,element_2]

# Dictionary
add = lambda x,y:x+y
subtract = lambda x,y:x-y
divide = lambda x,y:x/y if y!= 0 else print("Not valid") 
multiply = lambda x,y:x*y

mydict = {"+":add,"-":subtract,"/":divide,"*":multiply}

# match
match operator:
    case "+":
        print(mydict["+"](element_1,element_2))
    case "-":
        print(mydict["-"](element_1,element_2))
    case "/":
          print(mydict["/"](element_1,element_2)) 
        
    case "*":
        print(mydict["*"](element_1,element_2))
    case _:
        print("Invallid operator")               
