# Input mathematics score
M = float(input("Enter Mathematics score (Out of 100):"))

# Input Science score
S = float(input("Enter Science score (Out of 100):"))

# Input Hindi score
H = float(input("Enter Hindi score (Out of 100):"))

# Input English score
E = float(input("Enter English score (Out of 100):"))

#Total marks obtained
A = M + S + H + E

#To find the percentage
Sum = A / 400
Per = Sum * 100

#TO give remarks on the scores obtained
if Per >= 90:
    print("A")
if 80 <= Per <= 89:
    print("B")
if 70 <= Per <= 79:
    print("C")
if 60 <= Per <= 69:
    print("D")
if Per < 60:
    print("F")                 
