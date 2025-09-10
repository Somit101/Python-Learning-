Quiz = {"What is capital of India?":["1.Delhi","2.Mumbai","3.Kolkata","4.Goa"],"What is colour of the sun?":["1.White","2.Yellow","3.Black","4.Green"],"What is national animal of India?":["1.Tiger","2.Peacock","3.Monkey","4.Lion"],"Who is the Prime minister of India?":["1.Narendra modi","2.Amit Shah","3.Sachin Tendulkar","4.Rahul Gandhi"],"What is the colour of the sky?":["1.Blue","2.Black","3.Green","4.White"]}
Answers = ["Delhi","White","Tiger","Narendra modi","Blue"]
marks = 0
index = 0
for x,y in Quiz.items():
        print(x)
        print(y)
        Input = str(input("Answer = ")).capitalize()
        if Input in Answers[index]:
            marks +=  1
        index += 1    

    
match marks:
    case 4|5:
        print(marks,": Excellent")
    case 3:
        print (marks,": Good")
    case 2|1|0:
        print(marks,": Try again")  




        