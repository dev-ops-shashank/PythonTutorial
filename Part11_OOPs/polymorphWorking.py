class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def animal_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_sound(dog)  # Output: Buddy says Woof!
animal_sound(cat)  # Output: Whiskers says Meow!