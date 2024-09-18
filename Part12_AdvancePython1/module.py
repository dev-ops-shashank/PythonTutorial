def myFunc():
    print("Hello User!")

myFunc()
print(__name__)
# __name__ is a special variable in Python that holds the name of the current module.
# module is nothing but a '.py' file in python
# When a module is run directly, __name__ is set to "__main__".
# When a module is imported, __name__ is set to the name of the module (without the .py extension).