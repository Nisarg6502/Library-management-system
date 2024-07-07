"""
This module defines the core data structures used in the system: Book, User, and Checkout.
"""

class Book:
    """Represents a book with title, author name, ISBN, year"""
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def update_info(self, title=None, author=None, isbn=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn

    def __str__(self):
        return f"Book( Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available})"
    
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __str__(self):
        return f"User( Name: {self.name}, User ID: {self.user_id})"
    
class Checkout:
    def __init__(self, user, book):
        self.user = user
        self.book = book

    def __str__(self):
        user_name = self.user.name if isinstance(self.user, User) else 'Unknown User'
        book_title = self.book.title if isinstance(self.book, Book) else 'Unknown Book'
        return f"Checkout(user='{user_name}', book='{book_title}')"