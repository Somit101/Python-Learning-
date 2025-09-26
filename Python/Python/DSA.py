# map and split
#(we can ask for more than one input in a line with the help of map and can split the outputs with help of split function)
A,B,C = map(int,input("Enter numbers: ").split())
print(A,B,C)


#(If we use sting we do not need to use map)
H,I,J = input("Enter the string: ").split()
print(H,I,J)


# Count digits
n = 56765
count = 0
while n>0:
    n = n//10
    count += 1
print(count) 

from math import *
def countdigit(num):
    return int(log10(num) + 1)
print(countdigit(2345))


# Check if palindrome or not
n = 1111
num = n
result = 0
while num>0:
    integer = num // 10
    fractional = num % 10
    num = integer
    result = result*10 + fractional
if n == result:
    print("True") 
else:
    print("False")

# Armstrong number
# Without converting to string - T.C.=O(logn base 10) [Even if we are making the loop run twice the T.C. can be written as the same]S.C.=O(1)
n = int(input("Enter the number: "))    
count = 0
num5 = n
while num5 > 0:
    num3 = num5 // 10
    num = num5 % 10
    num5 = num3  
    count += 1
result = 0
while n > 0:
    num1 = n // 10
    num2 = n % 10
    pro = (num2)**count
    result = result + pro
    n = num1
print(result)    

# With converting into string - T.C.=O(logn base 10) S.C.=O(1)
n = int(input("Enter the number: "))    
s = len(str(n))
result = 0
while n > 0:
    num1 = n // 10
    num2 = n % 10
    pro = (num2)**s
    result = result + pro
    n = num1
print(result)


# Factors of given number - T.C.=O(N) S.C.=O(k) [where k is the number of integers in mylist]
N = int(input("Enter the number: "))
mylist = []
for i in range(1,N+1):
    if N % i == 0:
        mylist.append(i)
print(mylist)

# Factors of given number (Lesser time complexity) - T.C.=O(N/2) [which is almost same as O(N)] S.C.=O(k) [where k is the number of integers in mylist]
N = int(input("Enter the number: "))
mylist = []
for i in range(1,int(N/2)+1):
    if N % i == 0:
        mylist.append(i)
mylist.append(N)        
print(mylist)

# Factors of given number (Optimised version) - T.C.=O(sqrt(num)) S.C.=O(k) [where k is the number of integers in mylist]
from math import sqrt
num = int(input("Enter your number: "))
mylist = []
for i in range(1,int(sqrt(num))+1):
    if num % i == 0:
        num1 = int(num/i)
        mylist.append(i)
        mylist.append(num1)
print(mylist)


# Storing frequency in dictionary (T.C. is very high)
mylist = [5,5,1,2,9,8,8,7,1,2,3,6,9,5,4,7,8]
mydict = {}
my_list = []
for i in mylist: # ()
    if i not in my_list:
      my_list.append(i)
print(my_list)  
for i in my_list: # ()
   if i in mylist:
      mydict.update({f"{i}":f"{mylist.count(i)}"})    
print(mydict)

# Storing frequency in dictionary (Lesser T.C.)
mylist = [5,5,1,2,9,8,8,7,1,2,3,6,9,5,4,7,8]
mydict = {}
for i in range(0,len(mylist)):
    if mylist[i] in mydict:
        mydict[mylist[i]] += 1
    else:
        mydict[mylist[i]] = 1
print(mydict)

