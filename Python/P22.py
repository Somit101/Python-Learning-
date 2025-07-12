N = int(input("Enter number of students: "))
mylist = []
for i in range(N):
    n = int(input(f"Enter marks of student {i + 1} out of 100: "))
    mylist.append(n)

H = list(map(lambda x:"A" if x>=90 else "B" if x>=80 else "c" if x>=70 else "D" if x>=60 else "E" if x>=50 else "Fail",mylist))

print(H)