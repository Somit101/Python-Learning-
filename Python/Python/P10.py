Student_report = {"Student1":{"Name":"Somit","Marks":"97"},"Student2": {"Name":"Joker","Marks":"34"},"Student3":{"Name":"Himanshu","Marks":"86"}}
print(Student_report.items())
for x,obj in Student_report.items():
    print(x,";")
    for y in obj:
        print(y,":",obj[y])
    grade = ()
    marks = int(obj["Marks"])
    if marks >= 90:
       grade = "A (Pass)"
    elif marks >= 80:
        grade = "B (Pass)" 
    elif marks >= 70:
        grade = "C (Pass)"
    elif marks >= 60:
        grade = "D (Pass)"
    elif marks >= 50:
        grade = "E (Pass)"
    elif marks >= 40:
        grade = "F (Pass)"
    else:
        grade = "Fail"                      
    print("Grade",":",grade)  


    