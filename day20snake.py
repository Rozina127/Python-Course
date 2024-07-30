from turtle import Turtle  # Import Turtle class from the turtle module

# Constants for initial snake positions and movement directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []  # List to store snake segments
        self.create_snake()  # Initialize the snake
        self.head = self.segments[0]  # Reference to the head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)  # Create initial segments

    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new segment
        new_segment.color("white")  # Set the segment color
        new_segment.penup()  # Lift the pen to avoid drawing lines
        new_segment.goto(position)  # Place the segment at the given position
        self.segments.append(new_segment)  # Add the segment to the list

    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add a new segment to the end of the snake

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the pre segment
            self.segments[seg_num].goto(new_x, new_y)  # Move the segment to the new position
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        if self.head.heading() != DOWN:  # Prevent the snake from moving in the opposite direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
