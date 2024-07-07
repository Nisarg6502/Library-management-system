# # Global list to store books
# books = []

# def add_book(title, author, isbn):
#     books.append({"title": title, "author": author, "isbn": isbn})

# def list_books():
#     for book in books:
#         print(book)
from models import Book

class BookManager:
    def __init__(self, storage):
        self.storage = storage
        self.books = self.storage.load_books()

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        self.storage.save_books(self.books)
        return book

    def update_book(self, isbn, updated_info):
        for book in self.books:
            if book.isbn == isbn:
                for key, value in updated_info.items():
                    setattr(book, key, value)
                self.storage.save_books(self.books)
                return book
        raise ValueError(f"Book with ISBN {isbn} not found")

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.storage.save_books(self.books)

    def list_books(self):
        return self.books

    def search_books(self, criteria):
        return [book for book in self.books if any(
            getattr(book, key, '').lower() == value.lower() for key, value in criteria.items()
        )]
