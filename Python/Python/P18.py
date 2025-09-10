mylist = []
for i in range(5):
    n = int(input(f"Enter integer {i + 1}: "))
    mylist.append(n)

def ma():
     t = []
     for i in mylist:
         x = lambda a : a*3
        
         t.append(x(i))
     print(t)     
ma()
   
