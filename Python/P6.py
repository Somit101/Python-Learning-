H =(input("Enter your character"))

if len(H) != 1:
    print("Please enter only one character")
else :
    if H.islower() == True:
      print(H,"is lower case")
    elif H.isupper() == True:
      print(H,"is upper case")
    elif H.isdigit(): 
        print(H, "is digit ")
    else:
        print("It is a special character")
 

