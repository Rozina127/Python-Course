
#    something =     123 
#    parameter =     argument
def greet():
    print("Hello")
    print("How are you?")
    print("Where do you live?\n")

# Call the function to execute it
greet()

#function which take input 
def takename(name, location):
    print(f"Your name is {name}")
    print (f"You live in {location}\n")

# Call the function with a specific input
takename("Rozina", "Peshawar")


######**************** Pint area calculator  **********************################

def paint_area_calculator():
    # Get room dimensions
    length = float(input("\nEnter the length of the room in meters: "))
    width = float(input("Enter the width of the room in meters: "))
    height = float(input("Enter the height of the room in meters: "))
    
    # Get paint coverage
    coverage = float(input("Enter the paint coverage in square meters per liter: "))
    
    # Calculate the area to be painted (assuming 4 walls and a ceiling)
    wall_area = 2 * height * (length + width)
    ceiling_area = length * width
    total_area = wall_area + ceiling_area
    
    # Calculate the amount of paint needed
    paint_needed = total_area / coverage
    
    print(f"The total area to be painted is {total_area:.2f} square meters.")
    print(f"You will need {paint_needed:.2f} liters of paint.")

# Call the function
paint_area_calculator()




#####************************ Prime number ***********************#######

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Get user input
num = int(input("\nEnter a number: "))

# Check if the number is prime and print the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
    
    
    
####************************  Encryption and decryption code ***********************####


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    # Reverse the shift amount for decoding
    if cipher_direction == "decode":
        shift_amount *= -1
    
    for char in start_text:
        # Check if the character is in the alphabet list
        if char in alphabet:
            # Find the position of the character in the alphabet
            position = alphabet.index(char)
            # Calculate the new position with the shift amount
            new_position = position + shift_amount
            # Append the shifted character to the result
            end_text += alphabet[new_position]
        else:
            # If character is not in the alphabet (like numbers, symbols, spaces), keep it unchanged
            end_text += char
    
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Main code execution
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Ensure the shift amount is within the range of the alphabet length
shift = shift % 26

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

# Ask the user if they want to restart the program
restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
while restart == 'yes':
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

