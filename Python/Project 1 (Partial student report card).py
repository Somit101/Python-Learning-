G = ["Mathematics","Science","Hindi","English","Computer Science"]

def myfunc():
    Name = str(input("Enter name of student: "))
    M = []
    for i in range(5):
        m =  float(input(f"Enter marks for {G[i]}: "))
        M.append(m)

    Sum = sum(M)
    Percentage = (Sum/5)*100 

    print("\n",Name,":") 
    for i in range(5):
        print(G[i],": ",M[i])

       

    
    if Percentage >=90:
        print("A grade")
    elif Percentage >=80:
        print("B grade")
    elif Percentage >=70:
        print("C grade")  
    else:
        print("D grade")
    print("Percentage: ",Percentage)    
    
myfunc() 

myfunc()

     
                 



       
