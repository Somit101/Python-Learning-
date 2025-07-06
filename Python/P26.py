
student_report = {}
score = {}
Names =[]
for i in range(5):
    Name = str(input(f"Enter name of student {i+1}: "))
    Science = int(input(f"Enter marks in science of student {i+1}: "))
    Mathematics = int(input(f"Enter marks in mathematics of student {i+1}: "))
    English = int(input(f"Enter marks in english of student {i+1}: "))
    Marks = []
    Marks.append(Science)
    Marks.append(Mathematics)
    Marks.append(English)
    Marks_tuple = tuple(Marks)
    student_report.update({Name : Marks_tuple})

    Percentage = sum(student_report[Name])/3
    score.update({Name:Percentage})
    Names.append(Name)
    

Grades = list(map(lambda a: "A" if a>=90 else "B" if a>=80 else "C" if a>=70 else "D" if a>=60 else "E" if a>= 50 else "F" if a>=40 else ("Fail"),score.values()))

Passed_all = dict(filter(lambda f: all(marks >= 40 for marks in f[1]),student_report.items()))


Topper = dict(sorted(score.items(),key = lambda c:c[1] ,reverse = True))
print(Topper)

        
    
    