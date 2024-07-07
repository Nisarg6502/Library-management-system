# users = []

# def add_user(name, user_id):
#     users.append({"name": name, "user_id": user_id})

from models import User

class UserManager:
    def __init__(self, storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        self.storage.save_users(self.users)
        return user

    def update_user(self, user_id, updated_info):
        for user in self.users:
            if user.user_id == user_id:
                for key, value in updated_info.items():
                    setattr(user, key, value)
                self.storage.save_users(self.users)
                return user
        raise ValueError(f"User with ID {user_id} not found")

    def delete_user(self, user_id):
        initial_count = len(self.users)
        self.users = [user for user in self.users if user.user_id != user_id]
        if len(self.users) < initial_count:
            self.storage.save_users(self.users)
            return True
        return False

    def list_users(self):
        return self.users

    def search_users(self, criteria):
        return [user for user in self.users if any(
            getattr(user, key, '').lower() == value.lower() for key, value in criteria.items()
        )]
