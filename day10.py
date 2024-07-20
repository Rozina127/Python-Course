#**************** function with return statements ***************#
def takename(name, location):
    """Returns a formatted string with the name and location."""
    return f"Your name is {name}. You live in {location}."

# Call the function with a specific input and print the result
result = takename("Rozina", "Peshawar")
print(result)

#************** with multiple return values **********************#
def takename(first_name, last_name, location):
    """Returns a formatted string with the first name, last name, and location."""
    return f"Your name is {first_name} {last_name}. You live in {location}."

# Call the function with specific inputs and print the result
result = takename("Rozina", "Khan", "Peshawar")
print(result)
 
 #******** Calculator in python  by using function and dictionaries  *******#
 
def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract the second number from the first number."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide the first number by the second number."""
    if y == 0:
        return "Error: Division by zero."
    return x / y

# Dictionary to map operation names to functions
operations = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

def calculator():
    """Perform calculations based on user input."""
    print("Available operations: add, subtract, multiply, divide")
    
    operation = input("Enter the operation you want to perform:\n").lower()
    
    if operation not in operations:
        print("Invalid operation.")
        return
    
    # Get numeric inputs for the two numbers
    x = float(input("Enter the first number:\n"))
    y = float(input("Enter the second number:\n"))

    # Perform the operation and print the result
    result = operations[operation](x, y)
    print(f"The result of {operation} is: {result}")

# Run the calculator
calculator()
