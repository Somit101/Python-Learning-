Input = input("Enter shape name: ").capitalize()
match Input:
    case "Circle":
        print("Area = pi*r*r (r = radius)")
    case "Square":
        print("Area = a*a (a = side)")
    case "Rectangle":
        print("Area = l*b (l = length, b = breadth)")
    case "Triangle":
        print("Area = 0.5*base*height")           
    case _:
        print("Invalid")    