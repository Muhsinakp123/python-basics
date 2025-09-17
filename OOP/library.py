# Question 2 : Library Management System (OOP)

# Write a Python program using Object-Oriented Programming (OOP) concepts to create a simple Library Management System

class Book:
    def __init__(self, book_id, title, author, available_copies):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__available_copies = available_copies

    def get_title(self):
        return self.__title

    def book_info(self):
        """Display book details"""
        print(f"ID: {self.__book_id}, Title: {self.__title}, Author: {self.__author}, "
              f"Available Copies: {self.__available_copies}")

    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"You borrowed '{self.__title}'.")
        else:
            print(f"'{self.__title}' is not available right now.")

    def return_book(self):
        self.__available_copies += 1
        print(f"You returned '{self.__title}'.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\n--- Library Books ---")
            for book in self.books:
                book.book_info()

    def search_book(self, title):
        found_books = []
        for book in self.books:
            if book.get_title().lower() == title.lower():
                found_books.append(book)
        return found_books


# create library
library = Library()

# Adding sample books
book1 = Book(1, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 5)
book2 = Book(2, "The Hobbit", "J.R.R. Tolkien", 3)
book3 = Book(3, "1984", "George Orwell", 2)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Menu loop
while True:
    print("\nWelcome to the Library Management System")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Search for a book by title")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.list_books()

    elif choice == '2':
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        copies = int(input("Enter Available Copies: "))
        new_book = Book(book_id, title, author, copies)
        library.add_book(new_book)
        print(f"Book '{title}' added successfully.")

    elif choice == '3':
        title = input("Enter the book title to search: ")
        found_books = library.search_book(title)
        if found_books:
            for book in found_books:
                book.book_info()
        else:
            print(f"No books found with the title '{title}'.")

    elif choice == "4":
        title = input("Enter book title to borrow: ")
        found_books = library.search_book(title)
        if found_books:
            found_books[0].borrow_book()
        else:
            print("Book not found.")

    elif choice == "5":
        title = input("Enter book title to return: ")
        found_books = library.search_book(title)
        if found_books:
            found_books[0].return_book()
        else:
            print("Book not found.")

    elif choice == '6':
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")

