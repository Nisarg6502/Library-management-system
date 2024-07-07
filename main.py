
from storage import Storage
from book import BookManager
from user import UserManager
from check import CheckoutManager

"""
Library Management System

This file contains the main class which controls the entire application by integrating the modules of book, user and check.
Features a command line interface for input and output
Logic of each manager is handled by its respective module
"""

class LibraryManagementSystem:
    def __init__(self):
        self.storage = Storage()
        self.book_manager = BookManager(self.storage)
        self.user_manager = UserManager(self.storage)
        self.checkout_manager = CheckoutManager(self.storage, self.book_manager, self.user_manager)

    def display_menu(self):
        print("""\nLibrary Management System
        1. Add Book
        2. Update Book
        3. Delete Book
        4. List Books
        5. Search Books
        6. Add User
        7. Update User
        8. Delete User
        9. List Users
        10. Search Users
        11. Checkout Book
        12. Check-in Book
        13. List Checkouts
        0. Exit""")

    #Menu driven library for choices and the Main loop of the program.
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    self.add_book()
                elif choice == '2':
                    self.update_book()
                elif choice == '3':
                    self.delete_book()
                elif choice == '4':
                    self.list_books()
                elif choice == '5':
                    self.search_books()
                elif choice == '6':
                    self.add_user()
                elif choice == '7':
                    self.update_user()
                elif choice == '8':
                    self.delete_user()
                elif choice == '9':
                    self.list_users()
                elif choice == '10':
                    self.search_users()
                elif choice == '11':
                    self.checkout_book()
                elif choice == '12':
                    self.checkin_book()
                elif choice == '13':
                    self.list_checkouts()
                elif choice == '0':
                    print("Thank you for using the Library Management System. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError as e:
                print(f"Error: {str(e)}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = self.book_manager.add_book(title, author, isbn)
        print(f"Book added successfully: {book}")

    def update_book(self):
        isbn = input("Enter ISBN of the book to update: ")
        title = input("Enter new title (press enter to skip): ")
        author = input("Enter new author (press enter to skip): ")
        updated_info = {}
        if title:
            updated_info['title'] = title
        if author:
            updated_info['author'] = author
        book = self.book_manager.update_book(isbn, updated_info)
        print(f"Book updated successfully: {book}")

    def delete_book(self):
        isbn = input("Enter ISBN of the book to delete: ")
        self.book_manager.delete_book(isbn)
        print("Book deleted successfully")

    def list_books(self):
        books = self.book_manager.list_books()
        for book in books:
            print(book)

    def search_books(self):
        print("Enter search criteria (press enter to skip):")
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        criteria = {}
        if title:
            criteria['title'] = title
        if author:
            criteria['author'] = author
        if isbn:
            criteria['isbn'] = isbn
        books = self.book_manager.search_books(criteria)
        for book in books:
            print(book)

    def add_user(self):
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        user = self.user_manager.add_user(name, user_id)
        print(f"User added successfully: {user}")

    def update_user(self):
        user_id = input("Enter ID of the user to update: ")
        name = input("Enter new name (press enter to skip): ")
        updated_info = {}
        if name:
            updated_info['name'] = name
        user = self.user_manager.update_user(user_id, updated_info)
        print(f"User updated successfully: {user}")

    def delete_user(self):
        user_id = input("Enter ID of the user to delete: ")
        if self.user_manager.delete_user(user_id):
            print("User deleted successfully")
        else:
            print(f"No user found with ID {user_id}")

    def list_users(self):
        users = self.user_manager.list_users()
        for user in users:
            print(user)

    def search_users(self):
        print("Enter search criteria (press enter to skip):")
        name = input("Name: ")
        user_id = input("User ID: ")
        criteria = {}
        if name:
            criteria['name'] = name
        if user_id:
            criteria['user_id'] = user_id
        users = self.user_manager.search_users(criteria)
        for user in users:
            print(user)

    def checkout_book(self):
        user_id = input("Enter user ID: ")
        isbn = input("Enter book ISBN: ")
        checkout = self.checkout_manager.checkout_book(user_id, isbn)
        print(f"Book checked out successfully: {checkout}")

    def checkin_book(self):
        isbn = input("Enter ISBN of the book to check in: ")
        try:
            book = self.checkout_manager.checkin_book(isbn)
            print(f"Book checked in successfully: {book}")
        except ValueError as e:
            print(f"Error: {e}")

    def list_checkouts(self):
        checkouts = self.checkout_manager.list_checkouts()
        for checkout in checkouts:
            print(checkout)

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.run()