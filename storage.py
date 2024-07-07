import json
from models import Book, User, Checkout

class Storage:
    def save_data(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, default=lambda o: o.__dict__, indent=2)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                      return json.load(f)
        
        except FileNotFoundError:
             return []
        # except (IOError, json.JSONDecodeError) as e:
        #     print(f"Error loading data from {filename}: {e}")

    def save_books(self, books):
         self.save_data([book.__dict__ for book in books], 'books.json')

    def load_books(self):
         data = self.load_data('books.json')
         return [Book(**book) for book in data]
    
    def save_users(self, users):
         self.save_data([user.__dict__ for user in users], 'users.json')

    def load_users(self):
         data = self.load_data('users.json')
        #  return [User(**user) for user in data]
         return [User(user['name'], user['user_id']) for user in data]
    
    def save_checkout(self, checkouts):
        checkout_data = [
        {
            'user': {'name': checkout.user.name, 'user_id': checkout.user.user_id},
            'book': {'title': checkout.book.title, 'author': checkout.book.author, 'isbn': checkout.book.isbn, 'available': checkout.book.available}
        } for checkout in checkouts
        ]
        self.save_data(checkout_data, 'checkouts.json')

    def load_checkouts(self):
        data = self.load_data('checkouts.json')
        checkouts = []
        for checkout in data:
            try:
                user_data = checkout['user']
                book_data = checkout['book']
                user = User(user_data['name'], user_data['user_id'])
                book = Book(book_data['title'], book_data['author'], book_data['isbn'], book_data['available'])
                checkouts.append(Checkout(user, book))
            except KeyError as e:
                print(f"Skipping invalid checkout data: {e}")
        return checkouts