
student1 = {}
student2 = {}
student3 = {}
student4 = {}
student5 = {}
students={"child1":student1,"child2":student2,"child3":student3,"child4":student4,"child5":student5}
def my_func():
    for x in students:
             H = input("Enter name of student : ")
             I = int(input("Enter marks in Science : "))
             J = int(input("Enter marks in Mathematics : "))
             K = int(input("Enter marks in English : "))
             L = int(input("Enter marks in Hindi : "))
             M = int(input("Enter marks in Computer : "))
             Total = I+J+K+L+M
             percentage = Total/5
             students[x].update({"Name":H})
             students[x].update({"Science":I})
             students[x].update({"Mathematics":J})
             students[x].update({"English":K})
             students[x].update({"Hindi":L})
             students[x].update({"Computer":M})
             students[x].update({"Total":Total})
             students[x].update({"Percentage":percentage})

             

             if percentage >= 90:
                  grade = ("A grade")
             elif percentage >= 80:
                 grade = ("B grade")
             elif percentage >= 70:
                  grade = ("C grade")
             elif percentage >= 60:
                 grade = ("D grade")
             elif percentage >= 50:
                  grade = ("E grade")  
             elif percentage >= 40:
                  grade = ("F grade")       
             else:
                 grade = ("Fail")
             students[x].update({"Grade":grade})     

    for key,value in students.items():
         print(f"\n{key}: ")
         for v,m in value.items() :
              print(f"\n{v}:",value[v])
                                     


my_func()    





  
    

    