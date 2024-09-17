
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):                          # Dog class Inheriting Animal Class
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):                          # Cat class Inheriting Animal Class
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!