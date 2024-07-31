from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.color("white")  # Set the color of the ball to white
        self.shape("circle")  # Set the shape of the ball to a circle
        self.penup()  # Lift the pen to prevent drawing lines
        self.x_move = 3  # Set the initial x-axis movement speed
        self.y_move = 3  # Set the initial y-axis movement speed
        self.move_speed = 0.03  # Initial speed of the ball

    def move(self):
        new_x = self.xcor() + self.x_move  # Calculate the new x-coordinate
        new_y = self.ycor() + self.y_move  # Calculate the new y-coordinate
        self.goto(new_x, new_y)  # Move the ball to the new position

    def bounce_y(self):
        self.y_move *= -1  # Reverse the y-axis movement direction

    def bounce_x(self):
        self.x_move *= -1  # Reverse the x-axis movement direction
        self.move_speed *= 0.9  # Speed up the ball

    def reset_position(self):
        self.goto(0, 0)  # Move the ball to the center of the screen
        self.move_speed = 0.03 # Reset the ball speed
        self.bounce_x()  # Change the ball's direction
