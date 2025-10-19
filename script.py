class Pet:
    def speak(self):
        print("I am a Pet")

class Dog(Pet):
    def speak(self):
        print("I am a dog")

animal1 = Dog()

animal1.speak()

animal2 = Pet()

animal2.speak()