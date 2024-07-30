from turtle import Turtle  # Import Turtle class from the turtle module
import random  # Import the random module

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape of the food
        self.color("green")  # Set the color of the food
        self.penup()  # Lift the pen to avoid drawing lines
        self.speed("fastest")  # Set the speed to the fastest for instant movements
        self.refresh()  # Move the food to a random position

    def refresh(self):
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new random position
