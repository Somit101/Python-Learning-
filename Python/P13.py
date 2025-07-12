report = {"Somit":[89,97,88,90,91],"Nagesh":[78,87,88,76,90],"Kartik":[97,94,90,78,77]}
for i in report:
    print(i,"=")
    total = sum(report[i])
    print("Total marks:",total)
    percentage = total / 5
    print("Percentage:",percentage)

    grade = ()

    if total >= 90:
       grade = "A (Pass)"
    elif total >= 80:
        grade = "B (Pass)" 
    elif total >= 70:
        grade = "C (Pass)"
    elif total >= 60:
        grade = "D (Pass)"
    elif total >= 50:
        grade = "E (Pass)"
    elif total >= 40:
        grade = "F (Pass)"
    else:
        grade = "Fail"                      
    print("Grade",":",grade)    


