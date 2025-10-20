class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}{lname}@outlook.com"

user1 = Person("Diego", "Martin")

print(user1.email)