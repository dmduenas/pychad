class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"This is a {self.name}. He is {self.age} years old")

class Dog(Pet):
    def speak(self):
        print("Woof Woof")

class Cat(Pet):
    def speak(self):
        print("Meow Meow")

animal1 = Pet("Ace", 19)
animal1.show()

animal2 = Dog("Snoopy", 23)
animal2.show()

animal3 = Cat("Garfield", 4)
animal3.show()