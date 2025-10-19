class Pet:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Pet):
    def __init__(self, name, color):
        super().__init__(name, color)

class Dog(Pet):
    pass

animal1 = Cat("Garfield", "yellow")
animal2 = Dog("Snoopy", "white")

print(animal1.name)
print(animal2.name)