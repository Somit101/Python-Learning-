Info = []
for i in range(5):
    Name = str(input(f"Enter name of candidate {i+1}: "))
    Age = int(input(f"Enter age of {Name}: "))
    Data = Name,Age
    Data_tuple = tuple(Data)
    Info.append(Data_tuple)

Eligibility = list(filter(lambda b:b[1]>=18,Info))
print(Eligibility)

Order = sorted(Eligibility,key = lambda c:c[1],reverse = True)
print(Order)

with open("Voting.txt","a") as voting:
    voting.write(Eligibility)
    


    
