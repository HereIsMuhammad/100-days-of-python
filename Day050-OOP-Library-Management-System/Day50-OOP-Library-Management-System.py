# Day 50: OOP Project (Library Management System)

class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        book_id = input("Enter book ID: ")

        book = Book(title, author, book_id)
        self.books.append(book)

        print("Book added successfully!\n")

    def view_books(self):
        if len(self.books) == 0:
            print("No books in library.\n")
            return

        print("\nLibrary Books:")
        for book in self.books:
            book.display()
        print()

    def issue_book(self):
        book_id = input("Enter book ID to issue: ")

        for book in self.books:
            if book.book_id.lower() == book_id.lower():
                if book.is_issued:
                    print("Book already issued.\n")
                else:
                    book.is_issued = True
                    print("Book issued successfully.\n")
                return

        print("Book not found.\n")

    def return_book(self):
        book_id = input("Enter book ID to return: ")

        for book in self.books:
            if book.book_id.lower() == book_id.lower():
                if not book.is_issued:
                    print("Book was not issued.\n")
                else:
                    book.is_issued = False
                    print("Book returned successfully.\n")
                return

        print("Book not found.\n")

    def search_book(self):
        book_id = input("Enter book ID to search: ")

        for book in self.books:
            if book.book_id.lower() == book_id.lower():
                print("Book found:")
                book.display()
                print()
                return

        print("Book not found.\n")


def show_menu():
    print("====== Library Management System ======")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")


library = Library()

while True:
    show_menu()
    choice = input("Enter choice (1-6): ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.search_book()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice\n")