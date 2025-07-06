G = []
for i in range(5):
    g = int(input(f"Enter marks of student {i + 1}: "))
    G.append(g)
H = sum(G)
print(H)
print(H/5)   
