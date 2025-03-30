class UserNotFoundError(Exception):
    pass


class WrongPasswordError(Exception):
    pass


class UserAuth:
    def __init__(self, dane):
        self.dane=dane

    def login(self, username, password):
        if username in self.dane.keys():
            if password == self.dane[username]:
                return print("Success")
            else:
                raise WrongPasswordError("Wrong password")
        else:
            raise UserNotFoundError("User not found")




