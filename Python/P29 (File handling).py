with open("Story.txt","w") as story:
    story.write("I am the best\nI am MR CEO")
    

with open("Story.txt","r") as f:
    content = f.read() # This takes the cursor to the end so if i perform readlines after this it will be empty 
    word = content.split()
    #lines = f.readline()
    H = len(word)
    M = len(content)

with open("Story.txt","r") as m:
    lines = m.readlines()
        
    
print(H)  
print(M)      
print(len(lines))    
print(content)
