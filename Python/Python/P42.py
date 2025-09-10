class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN number: {self.ISBN}" 

     
Mylibrary = [ Book("Python","Somit","1478526930125"),
 Book("Rich","Robert","6541230825794"),
 Book("Influence","Mike","021485693512")  ]  

def search_by_author():
       User_input = input("Enter the name of author: ").strip().capitalize()
       print(f"Books by {User_input}: ")

       found = False
       for book in Mylibrary:

          if book.author == User_input:
             print(book.title)  
             found =True
       if not found:
            print("No books by the author")

def show_all_books():
    print("All books in library: ")
    for book in Mylibrary:
            print(f"- {book.title}")

def search_by_ISBN():
          isbn_number = input("Enter ISBN number of the book you want to see: ")
          print(f"Book with ISBN number {isbn_number}: ")

          found = False
          for book in Mylibrary:
               if book.ISBN == isbn_number:
                    print(book)
                    found = True
          if not found:
               print("No book found with that ISBN.")
                        
def menu():
     print("\nLibrary: ")
     print("1.Show all books")
     print("2.Search book by author")
     print("3.Search book by ISBN number")
     print("4.Exit")

while True:
     menu()
     Task = int(input("What do you want to do? (1,2,3): "))
     if Task == 1:
          show_all_books()
     elif Task == 2:
          search_by_author()
     elif Task == 3:
          search_by_ISBN()
     elif Task == 4:
          break     
     else:
          print("Invalid task to perform")               






    


