
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
    print (f"You live in {location}")

# Call the function with a specific input
takename("Rozina", "Peshawar")


###### Pint area calculator 
def paint_area_calculator():
    # Get room dimensions
    length = float(input("Enter the length of the room in meters: "))
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
