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
 
 
 