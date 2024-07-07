# checkouts = []

# def checkout_book(user_id, isbn):
#     checkouts.append({"user_id": user_id, "isbn": isbn})
from models import Checkout, Book

class CheckoutManager:
    def __init__(self, storage, book_manager, user_manager):
        self.storage = storage
        self.book_manager = book_manager
        self.user_manager = user_manager
        self.checkouts = self.storage.load_checkouts()

    def checkout_book(self, user_id, isbn):
        user = next((user for user in self.user_manager.users if user.user_id == user_id), None)
        book = next((book for book in self.book_manager.books if book.isbn == isbn), None)

        if not user:
            raise ValueError(f"User with ID {user_id} not found")
        if not book:
            raise ValueError(f"Book with ISBN {isbn} not found")
        if not book.available:
            raise ValueError(f"Book with ISBN {isbn} is not available")

        checkout = Checkout(user, book)
        book.available = False
        self.checkouts.append(checkout)
        self.storage.save_checkout(self.checkouts)
        self.book_manager.storage.save_books(self.book_manager.books)
        return checkout

    def checkin_book(self, isbn):
        checkout = next((c for c in self.checkouts if isinstance(c.book, Book) and c.book.isbn == isbn), None)
        if not checkout:
            raise ValueError(f"No checkout found for book with ISBN {isbn}")
        checkout.book.available = True
        self.checkouts.remove(checkout)
        self.storage.save_checkout(self.checkouts)
        self.book_manager.storage.save_books(self.book_manager.books)
        return checkout.book

    def list_checkouts(self):
        return self.checkouts