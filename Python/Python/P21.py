mylist = []
for i in range(5):
    n = str(input(f"Enter name {i+1}: "))
    mylist.append(n)


H = list(map(lambda m:m,mylist))
H.sort(key = len)      
print(H)