Report = {}
Num = int(input("How many students you want to add?: "))
for i in range(Num):
    Name = str(input(f"Enter name of student {i+1}: "))
    Mathematics = (input(f"Enter marks in mathematics of {Name}: "))
    Science = (input(f"Enter marks in science of {Name}: "))
    English = (input(f"Enter marks in english of {Name}: "))
    marks = []
    marks.append(Mathematics)
    marks.append(Science)
    marks.append(English)
    Report.update({Name:marks})
    Total = Mathematics+Science+English

with open("report.txt","w") as add:
    add.write("Students : Mathematics, Science, English\n")
    for student,scores in Report.items():
       
        line = f"{student}: {",".join(scores)}\n" # Use join statement if functions take only 1 value
        add.write(line) 

        
with open("report.txt","r") as read:
    print(read.read()) 
    

           