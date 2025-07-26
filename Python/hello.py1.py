
x = "I am the best" 
y = 5
z = 8
if y+z>=13:
    print(x)
if z>y:
        print(x)

x,y,z = "A" , "B" , "C"
print(x)
print(y)
print(z)        

Letters = ["A","B","C"]
a,b,c = Letters
print(a)
print(b)
print(c)

print(x+y+z)
print(x,y,z)

def myfunc():
      global x 
      x="Best"
      print("I am the" , x)
      print(x)
myfunc()      

print(x)

import random
print(random.randrange(1,10))

H = "I,AM,THE"
print(H[2+3])

# This is for loop it will not stop until everything is displayed and nothing is left
for x in "Somit":
      print(x)

print(len(H))

# This is to check a specific element in the string
L = "Iam, thebest"
print("best" in L)

print(L[:4])
print(L[-5:-3])

print(L.split(","))
print(L.upper())
print(L.strip())
print(L.replace("I", "J"))

# format string
age = 20
Y = f"my name is somit and i am {age}"
print(Y)
# Decimal place
U = f"my age is {age:.2f}"
print(U)

#Decimal place
I = 89.9798
print( round(I,2))

# Escape characters
L = "Iam \"you\" thebest"
print(L)

G = "\111\101\102\103"
print(G)
L = "Iam, \\thebest"
print(L)
#Single quote
L = "I\'am, thebest"
print(L)

#Backslash
K="Iam, \\thebest"
print(K)

#New line
J = "I\nam, thebest"
print(J)

#Carriage return
J = "I\ram, thebest"
print(J)

#Tab
J = "I\tam, thebest"
print(J)

#backspace
J = "I \bam, thebest"
print(J)

#form feed
J = "I  \fam, thebest"
print(J)

#Octal value
J = "\101\102\103\104\105"
print(J)

#hex value
J = "\x68\x78\x89"
print(J)

# String methods
K="  i am the best i am "


print(K.capitalize())
print(K.center(50,"-"))
print(K.count("i"))
print(K.encode())
print(K.swapcase())
print(K.find("am"))
print(K.rfind("am"))
print(K.index("b"))
print(K.islower())
print(K.isspace())
print(K.lstrip())
print(K.split(" "))
print(K.rsplit())

Z = "Jocker\nJockey"
print(Z.splitlines())
D = ["apple","tree","house","name"]
print('-'.join(D))                               #Join string
print(K.startswith(" "))                         
print(K.center(60,"-"))                             # .center(width,fillchar="")
H = "90"
print(H.zfill(7))
print(K.rjust(40))

print(bool("hello"))
print(bool(10))

V = 100
B = 60
print(V % B)
print(V ** B)
print(V // B)    #Greatest integer function after dividing

def god():
      return True
print(god())
print(type(10 > 5))

                                             # LIST
H = ['elephant','joker','man']
print(type(H))    
if "elephant" in H:
      print("Success")  

H[1] = "Human"
print(H)
H [0:1] = ['Him','Her']
print(H)
H [0:2] = ['elephant']
print(H)

#Insert
H.insert(2,'Goat')
print(H)
#Extend
Boy = ['Goat','Sheep','Cow']
Girl = ['Elephant','Sheep','Lion']
Boy.extend(Girl)
print(Boy)

#Remove
v = ["House","Home","Work"]
v.pop(1)
print(v)
v.pop()
print(v)
del v[0]
print(v)

#List Loop
N = ["Joker","Kal"]
for i in range(len(N)):
      print(N[i])
for x in N:
      print(x)      
print(len(N))

#list comprehension
M = ["apple","mango","banana","cherry"]
O = []
for x in M:
      if "a" in x:
            O.append(x)
print(O)            
# Short form
M = ["apple","mango","banana","cherry"]
O = []
O = [x for x in M if "a" in x]
print(O)
O = [x for x in M]
print(O)
L = "aaajjjhhh"
O = [x for x in range(0,10) if x < 5]
print(O)
O = [x.upper() for x in M]
print(O)
O = [x if x!= "banana" else "orange" for x in M]
print(O)

#Sort
M.sort(key=str.lower)
print(M)
M.sort(reverse=True)
print(M)

# Copy
O = M.copy()
print(O)
O = list(M)
print(O)
O = M[:]
print(O)

#Join
b = ["a","b","c"]
c = [1,2,3]
e = ["j","k","l"]
d = b+c
print(d)

for i in c:
      b.append(c)
print(b)  

                                                   #Tuples

mytuple = ("apple","orange","grapes")
mytuple = ("apple",)
# Change tuple values
t = ("Joker","Human","Animal")
p = list(t)
p[1] = "Man"
L = tuple(p)
print(L)

p = ("apple",)
t += p
print(t)
# unpacking tuples
thistuple = ('me','I','we')
(x,y,z) = thistuple
print(x)
print(y)
print(z)

(*x,y) = thistuple
print(x)
print(y)  

                                               # SETS
myset = {"apple","banana","cherry"}
for i in myset :
      print(i)

# Add items
myset.add("orange")
print(myset)

torque = {"motion","momentum"}
myset.update(torque)
print(myset)

myset.remove("orange")   # remove() will give an error if the item mentioned is not present in the set
myset.discard("orange")  # discard() will not give an error if the item mentioned is  not in the set
m = myset.pop()
print(m)
thisset = {"J","K","L"}
thisset.clear()


myset = {1,2,3}
mytuple = (4,5,6)
v = myset.union(mytuple)
print(v)
set1 = {"List","Tuple","Hard"}

set2 = {1,2,3,"Hard"}
set3 = {"Just","Hard","Work"}
set1.intersection_update(set2, set3)
print(set1)

set1.difference_update(set2, set3)
print(set1)

set1.symmetric_difference_update(set2)
print(set1)

mytime = "Towards me"
print(mytime.split(" "))

                                     # Dictionaries
mydict = {"Name": "Somit",
          "Age": "19",
          "Nationality": "Indian"}
print(mydict["Name"])
print(mydict.get("Age"))
print(mydict.keys())
print(mydict.items())
mydict["Gender"] = "Male"
mydict.update({"Age":"20"})
print(mydict)
mydict.popitem()
print(mydict)
for x in mydict:
      print(mydict[x])
for x in mydict.values():
      print(x)      
for x in mydict.items():
      print(x)
for x,y in mydict.items():
      print(x,":",y)      

# Nested dictionaries
family = { "class1":{"Name" : "Somit", "Age": "19"},"class2":{"Name":"Chirag","Age": "10"},"class3":{"Name":"Joker","Age":"100"} }

class1 = {"Name" :"Somit", "Age": "19"}
class2 = {"Name":"Chirag","Age": "10"}
class3 = {"Name":"Joker","Age":"100"}

family1 = {"Top":class1,"Middle":class2,"Lower":class3}

print(family1)
print(family1["Top"]["Name"])
print(family1.items())
for x, obj in family1.items():
      print(x)

      for y in obj:
            print(y,":",obj[y])


                                  # If... Else statements
a = 9
b = 9
print("A") if a>b else print("B")
print("A") if a>b else print("B") if a==b else print("C")   

# Match statement
name = "somit"
match name:
      case "somit":
            print("Success")
      case "Juggu":
            print("High")
      case "nuppu":
            print("Low")  
      case _:
            print("None")                

date = int(input("Enter date of birth: "))
match date:
      case 1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|29|30:
            print("Normal day")
      case 28:
            print("Happy birthday!!!")   
      case _:
            print("Invalid")         

                                               # Functions
def my(*kids):
      print("The youngest child ", kids)
my("Somit","Sumit","Rahul")      

def my_(**kid):
      print(kid)
my_(child1 = "Somit",child2 = "Joker")    

def god(x,/):
      print(x)
god(3)    

def good(*,x):
      print(x)
good(x = 0)      

def good_god(a,b,/,*,c,d):
      print(a+b+c+d)
good_god(5,66,c=4,d=9)      

def no(country = "India"):
      print("I am from "+ country)
no("Sweden")
no() 
no("India")  

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

                                            # Lambda
x = lambda a : a + 10
print(x(5))

x = lambda a,b : a*b 
print(x(5,6))

def myfunc(n):
      return lambda a: a*n 
mydoubler = myfunc(2)
print(mydoubler(11))

# map()
mylist = [1,2,3,4]
def me():
      H = list(map(lambda a:a*3 , mylist)) # This means that for every a in mylist multiply it by 3 so basically a loop
      print(H)
me()

# filter()
def him():
      G = list(filter(lambda x : x%2 == 0,mylist)) # this means in mylist if x is even return x
      print(G)
him()

# sorted()
F = sorted(mylist, key = lambda a:a,reverse = True )
print(F)

                                                # OOP
# __init__
class person:
      def __init__ (self,name,age):
            self.name = name
            self.age = age 
      def __str__(self):
            return f"Name = {self.name}\nAge = {self.age}"     
p1 = person("Somit",19)
print(p1.name)
print(p1.age)                                                            

# __str__
class new:
      def __init__(me,dog,cat):
            me.dog = dog
            me.cat = cat 
      def __str__(me):
            return f"{me.dog} and {me.cat}"      
p2 = new("Duggu","mew")
p2.cat = "meow"
print(p2)      

# Inheritence
class Students(person):
      pass
S = Students("somit","18")
print(S.name)

class Students1(person):
      def __init__(self,age):
            self.age = age
S1 = Students1("19")
print(S1.age)

class Students2(person):
      def __init__(self,name,age):
            person.__init__(self,name,age)
S2 = Students2("Rahul","19")
print(S2.name)  
print(S2.age)          

class Students2(person):
      def __init__(self,name,age):
            super().__init__(name,age)
S2 = Students2("Rahul","19")
print(S2.name)  
print(S2.age)

#Iterator
class Mynum:
      def __iter__(self):
            self.a = 1
            return self
      def __next__(self):
            x = self.a
            if x<20:
               self.a +=1
               return x
            else:
                  raise StopIteration
myclass = Mynum()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter)) 
print(next(myiter))     

def Somit():
      x = "Somit"
      def Goat():
            nonlocal x
            x = "Happy"
            
      Goat()
      return x
print(Somit())
