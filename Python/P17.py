def organize_data():
    mylist = []
    for i in range(5):
        N = int(input(f"Enter integer{i + 1}: "))
        mylist.append(N)

    odd_count = 0
    even_count = 0    

    for i in mylist:
        if i%2 == 0:
           even_count += 1
        else:
           odd_count += 1

    print("Even numbers",":",even_count)
    print("Odd numbers",":",odd_count)
    print("Maximum value",":",max(mylist))
    print("Minimum value",":",min(mylist))
    
organize_data()

