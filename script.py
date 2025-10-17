class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

user1 = User("Batman", "bat@gmail.com")
user2 = User("Superman", "clarke@outlook.com")

print(f"{user1.username} is the number is the first account created")
print(f"{user2.username} is the nunver is the second account created")
print(f"There are a total of {User.user_count} accounts created")