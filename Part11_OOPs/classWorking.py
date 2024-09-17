# Briefly explaining Classes in Python

class Dog:
    def __init__(self, name, breed):        # this is similar to Contruction in Java
        #  Its primary purpose is to initialize the attributes of an object when it's created.
        # It's automatically called when a new instance of a class is created.
        # It's used to set initial values for object attributes.
        # It can take parameters, allowing you to customize the initial state of objects.
        self.name = name
        self.breed = breed
    
    # The double underscores before and after a name (like __init__) are often referred to as 
    # "dunder" (double underscore). Methods or attributes with this naming convention are called 
    # "dunder methods" or "magic methods".


    def bark(self):                         # see bottom for explaination on 'self'
        print(f"{self.name} says Woof!")

# Creating objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Using object methods
dog1.bark()  # Output: Buddy says Woof!
dog2.bark()  # Output: Max says Woof!

'''Why did we use self as an argument in the function bark()?

The `self` parameter in Python methods is a crucial concept in object-oriented programming. 
Let's break down why we use `self`:

1. Instance Reference:
   `self` refers to the instance of the class that is calling the method. It's how the method knows which 
specific object it's working with.

2. Accessing Instance Attributes:
   `self` allows the method to access and modify the attributes of the specific instance. In this case, 
`self.name` refers to the `name` attribute of the particular dog object calling the `bark` method.

3. Python's Explicit Self:
   Unlike some other languages, Python uses explicit `self` as the first parameter in instance methods. 
This makes it clear that the method operates on an instance.

4. Method vs Function:
   Including `self` distinguishes a method (which is associated with a class) from a regular function.

5. Automatic Passing:
   When you call a method on an object (like `dog.bark()`), Python automatically passes the instance as 
the first argument. So `dog.bark()` is implicitly translated to `Dog.bark(dog)`.

Let's see an example to illustrate:

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} says Woof!")

buddy = Dog("Buddy")
max = Dog("Max")

buddy.bark()  # Output: Buddy says Woof!
max.bark()    # Output: Max says Woof!

In this example:
- When we call `buddy.bark()`, Python effectively calls `Dog.bark(buddy)`.
- Inside the `bark` method, `self` refers to the `buddy` instance, so `self.name` is "Buddy".
- Similarly, for `max.bark()`, `self` refers to the `max` instance.

If we didn't use `self`:
def bark():
    print(f"{name} says Woof!")  # This would raise an error

This wouldn't work because the method wouldn't know which dog's name to use.

Remember, while `self` is the conventional name, you could technically use any valid parameter name. 
However, using `self` is a strong convention in Python, and it's highly recommended for code 
readability and consistency.'''


'''Some common dunder methods include:

__init__(): Constructor
__str__(): String representation of the object
__len__(): Defines behavior for the len() function
__add__(): Defines behavior for the + operator
__eq__(): Defines behavior for the == operator

Example of another dunder method:
class Dog:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Dog named {self.name}"

buddy = Dog("Buddy")
print(buddy)  # Output: Dog named Buddy

In this example, __str__() defines how the object should be represented as a string, 
which is used when you print the object.
The use of double underscores for these special methods is a Python convention that helps avoid naming 
conflicts with user-defined methods. It signals to Python and to other programmers that these methods 
have a special meaning and behavior.
It's important to note that while you can define your own methods with double underscores, it's 
generally not recommended unless you're truly defining a special behavior that Python will use 
automatically. For regular methods, single underscores are often used for internal or private 
methods (though Python doesn't enforce true privacy).

'''