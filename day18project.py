import turtle as turtle_module  # Import the turtle module for creating graphics
import random  # Import the random module for generating random choices

turtle_module.colormode(255)  # Set the color mode to 255 for RGB colors
tim = turtle_module.Turtle()  # Create a turtle object named tim
tim.speed("fastest")  # Set the speed of the turtle to the fastest
tim.penup()  # Lift the pen to avoid drawing lines when moving
tim.hideturtle()  # Hide the turtle cursor

# List of RGB color tuples
color_list = [
    (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
    (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185),
    (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
    (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77),
    (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90),
    (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
    (107, 127, 153), (174, 94, 97), (176, 192, 209)
]

tim.setheading(225)  # Set the turtle's heading to 225 degrees
tim.forward(300)  # Move the turtle forward by 300 units
tim.setheading(0)  # Set the turtle's heading to 0 degrees (facing right)
number_of_dots = 100  # Define the number of dots to be drawn

for dot_count in range(1, number_of_dots + 1):  # Loop to draw the specified number of dots
    tim.dot(20, random.choice(color_list))  # Draw a dot with a random color from the list
    tim.forward(50)  # Move the turtle forward by 50 units

    if dot_count % 10 == 0:  # After every 10 dots, move to the next row
        tim.setheading(90)  # Set the turtle's heading to 90 degrees (facing up)
        tim.forward(50)  # Move the turtle forward by 50 units
        tim.setheading(180)  # Set the turtle's heading to 180 degrees (facing left)
        tim.forward(500)  # Move the turtle backward by 500 units
        tim.setheading(0)  # Set the turtle's heading to 0 degrees (facing right)

screen = turtle_module.Screen()  # Create a screen object to display the drawing
screen.exitonclick()  # Keep the screen open until it is clicked
