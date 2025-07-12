mylist = []
for i in range(7):
    n = int(input(f"Enter element {i+1}: "))
    mylist.append(n)

H = list(filter(lambda x: x%2 == 0 and x>50,mylist))
print(H)