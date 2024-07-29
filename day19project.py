from turtle import Turtle, Screen  # Import the Turtle and Screen classes from the turtle module
import random  # Import the random module for generating random distances

is_race_on = False  # Initialize a flag to check if the race has started
screen = Screen()  # Create a Screen object to control the turtle screen
screen.setup(width=500, height=400)  # Set up the screen width and height
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  # Prompt the user to make a bet on a turtle color
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of turtle colors
y_positions = [-70, -40, -10, 20, 50, 80]  # List of starting y positions for the turtles
all_turtles = []  # List to store all turtle objects

# Create 6 turtles
for index in range(6):
    turtle = Turtle(shape="turtle")  # Create a new turtle object with turtle shape
    turtle.penup()  # Lift the pen to avoid drawing lines when moving
    turtle.color(colors[index])  # Set the turtle's color based on the colors list
    turtle.goto(x=-650, y=y_positions[index])  # Move the turtle to the starting position
    all_turtles.append(turtle)  # Add the new turtle to the all_turtles list

if user_bet:
    is_race_on = True  # If the user has made a bet, start the race

while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 650:  # 230 is the x-coordinate where the finish line is (250 - half the width of the turtle)
            is_race_on = False  # Stop the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")  # Print a message if the user's bet matches the winning turtle's color
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")  # Print a message if the user's bet does not match the winning turtle's color

        # Make each turtle move a random amount
        rand_distance = random.randint(0, 10)  # Generate a random distance between 0 and 10
        turtle.forward(rand_distance)  # Move the turtle forward by the random distance

screen.exitonclick()  # Keep the screen open until it is clicked
