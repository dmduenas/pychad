class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

person1 = Person("Diego", 34)

person1.name = "Aswang"

person1.greet()