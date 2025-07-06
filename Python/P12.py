Inventory = {"Books":"15","Shirts":"6","Jeans":"7","Lowers":"4","Bikes":"3","Cars":"0","Humans":"4","Dog":"1","Electronics":"16"}

def menu():
    print("\nInventory")
    print("1. Update items")
    print("2. View items")
    print("3. Remove items")
    print("4. Exit")

def update_item():
    H = input("Enter item to be added: ")
    I = input("Enter quantity: ")
    Inventory.update({H:I}) 
    print("Item added successfully") 

def view_items():
    for i in Inventory:
        print(i,":",Inventory[i])

def remove_items():
    J = input("Enter item to be removed: ")
    Inventory.pop(J)
    print("Item removed successfully")


while True:
    menu()
    Input = input("What do you want to do? (1,2,3) : ")
    if Input == "1":
        update_item()
    elif Input == "2":
        view_items()
    elif Input == "3":
        remove_items()
    elif Input == "4":
        break    

    else :
        print("Invalid task to perform")        



   