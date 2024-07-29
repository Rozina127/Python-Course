# higher order function are the functions that works woth other functions 



#******************************* Turtle movement project *************************************#
from turtle import Turtle, Screen  # Import the Turtle and Screen classes from the turtle module
tim = Turtle()  # Create a Turtle object named tim
screen = Screen()  # Create a Screen object to control the turtle screen

def move_forwards():
    tim.forward(10)  # Move the turtle forward by 10 units

def move_backwards():
    tim.backward(10)  # Move the turtle backward by 10 units

def turn_left():
    tim.left(10)  # Turn the turtle left by 10 degrees

def turn_right():
    tim.right(10)  # Turn the turtle right by 10 degrees

def clear():
    tim.clear()  # Clear the turtle's drawings
    tim.penup()  # Lift the pen to avoid drawing when moving to the home position
    tim.home()  # Move the turtle to the center of the screen
    tim.pendown()  # Put the pen down to resume drawing

screen.listen()  # Listen for key presses
screen.onkey(move_forwards, "f")  # Call move_forwards function when "f" key is pressed
screen.onkey(move_backwards, "b")  # Call move_backwards function when "b" key is pressed
screen.onkey(turn_left, "l")  # Call turn_left function when "l" key is pressed
screen.onkey(turn_right, "r")  # Call turn_right function when "r" key is pressed
screen.onkey(clear, "c")  # Call clear function when "c" key is pressed
screen.exitonclick()  # Keep the window open until it is clicked

