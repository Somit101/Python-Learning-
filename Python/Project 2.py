Books = []

def menu():
    print("\nLibrary menu:")
    print("1. Add book")
    print("2. Remove book")
    print("3. Search book")
    print("4. View books")
    print("5. Exit")

def add_book():
    book_to_add = input("Enter book to be added: ").lower()   
    Books.append(book_to_add)
    print("Book added successfully")

def remove_book():
    book_to_remove = input("Enter book to be removed: ").lower()
    if book_to_remove in Books:
         Books.remove(book_to_remove)
         print("Book removed successfully")
    else:    
        print("Book not found")

def search_book():
    book_to_search = input("Enter name of book: ").lower()
    if book_to_search in Books:
        print(book_to_search,"available")
    else:
        print(book_to_search,"not available")

def view_books():
    print("\n",Books)

while True:
    menu()
    Input = input("What do you want to do? : ")
    if Input == "Add book" :
        add_book()
    elif Input == "Remove book" :
        remove_book()
    elif Input == "Search book" :
        search_book()
    elif Input == "View books" :
        view_books()
    elif Input == "Exit" :
        print("Exit successfull")    
        break
    else:
        print("Invalid task to perform")   
                                    

   
    