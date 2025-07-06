mydict = {}
for i in range(4):
    n = str(input(f"Enter name {i + 1}: "))
    m = int(input(f"Enter integer {i + 1}: "))
    mydict.update({n:m})

keys = list(mydict.keys())
values = list(mydict.values())

H = list(map(lambda m : m **2,values))
print(H)

