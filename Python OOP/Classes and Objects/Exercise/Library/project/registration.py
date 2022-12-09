from Exercise.Library.project.library import Library
from Exercise.Library.project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user.username not in [x.username for x in library.user_records]:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user.username in [x.username for x in library.user_records]:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        for user in library.user_records:
            if user.user_id == user_id and user.username != new_username:
                if user.username in library.rented_books:
                    library.user_records[new_username] = library.user_records.pop(user.username)
                user.username = new_username
                return f"Username successfully changed to: {new_username} for user id: {user_id}"

            elif user.user_id == user_id and user.username == new_username:
                return "Please check again the provided username - it should be different than the username used so far!"

            elif not [x for x in library.user_records if x.user_id == user_id]:
                return f"There is no user with id = {user_id}!"
