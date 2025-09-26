class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN number: {self.ISBN}" 

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        
        self.books.append(book)

    def show_all_books(self):
        if not self.books:
            print("Library is empty")
        else:
            for book in self.books :
                print(f"- {book.title}")
            print("")    

    def search_by_author(self):
        Author_name = input("Enter name of author: ")
        found = False
        for book in self.books:
            if book.author == Author_name:
                print(f"* {book.title}")
                
                found = True
        print("")

        if not found:
            print("No book available from this author.")
            print("")
            

    def search_by_ISBN(self):
        ISBN_number = input("Enter ISBN number of the book: ")
        found = False
        for book in self.books:
            if book.ISBN ==  ISBN_number:
                print(book)
                found = True
        print("")
        if not found:
            print(f"No book available with {ISBN_number} as ISBN number.")      
            print("")  

B1 = Book("Python","Somit","1478526930125")
B2 = Book("Rich","Robert","6541230825794")
B3 = Book("Influence","Mike","021485693512")

library = Library()
library.add_book(B1)
library.add_book(B2)
library.add_book(B3)

print("All books in library: ")
library.show_all_books()


library.search_by_author()

library.search_by_ISBN()


                        