# Taking inputs
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Creating a dictionary to perform operations
operations = {
    "+": num1 + num2,
    "-": num1 - num2,
    "*": num1 * num2,
    "/": num1 / num2
}

# Display the result by accessing the dictionary
print(f"Result: {num1} {operator} {num2} = {operations[operator]}")
