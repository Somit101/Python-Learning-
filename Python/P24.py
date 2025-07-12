students = [("Soumitra", 92), ("Harsh", 85), ("Ravi", 70), ("Kajal", 48), ("Anu", 96)]

Pass_list = list(filter(lambda a:a[1]>=60,students))
print(Pass_list)

Marking = list(map(lambda b: ("A",b[0]) if b[1] >= 90 else ("B",b[0]) if b[1] >= 80 else ("C",b[0]) if b[1] >=70 else ("D",b[0]) if b[1] >= 60 else ("Fail",b[0]) ,students))
print(Marking)

for grade,name in Marking:
    print(name,":",grade)






