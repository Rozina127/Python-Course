from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()  # Initialize the Turtle class
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle to the desired size
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(position)  # Move the paddle to the given position

    def go_up(self):
        new_y = self.ycor() + 20  # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    def go_down(self):
        new_y = self.ycor() - 20  # Calculate the new y-coordinate
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position
