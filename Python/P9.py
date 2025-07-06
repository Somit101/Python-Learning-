J = []
for i in range(6):
    j = int(input(f"Enter number {i + 1}: "))
    J.append(j)

odd = 0
even = 0

for i in J:
    if i%2 == 0:
        even += 1
    else :
        odd += 1

print(f"Even numbers: {even}")      
print(f"Odd numbers: {odd}")      
