students = [
    ("Soumitra", 92, "Math"),
    ("Harsh", 85, "Science"),
    ("Ravi", 70, "English"),
    ("Kajal", 48, "Math"),
    ("Anu", 96, "English"),
    ("Vijay", 88, "Science"),
    ("Meena", 74, "Math"),
    ("Nina", 59, "English")
]

Filter = list(filter(lambda a:a[1]>=75,students))
print(Filter)

Sort = (sorted(students,key = lambda b:b[1],reverse = True))
print(Sort)

Performance = list(map(lambda c: ("A",c[0],c[2]) if c[1] >= 90 else ("B",c[0],c[2]) if c[1] >= 80 else ("C",c[0],c[2]) if c[1] >= 70 else ("D",c[0],c[2]) if c[1] >=60 else ("Fail",c[0],c[2]),students))
print(Performance)

for grades,name,subject in Performance:
    print(name,f"({subject})",":",grades)