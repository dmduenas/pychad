class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

user1 = User("Bruce", "bat@gmail.com", "123")

print(user1.email)
user1.email = "newmail@yahoo.com"
print(user1.email)