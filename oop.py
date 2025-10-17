class User():
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        return self._email.upper()

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email



user1 = User("Bruce", "Bat@gmail.com", "abc")
user2 = User("Clarke", "superman@outlook.com", "123")

print(user1.email)