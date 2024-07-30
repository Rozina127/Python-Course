from turtle import Screen  # Import Screen class from the turtle module
from day20snake import Snake  # Import the Snake class from day20snake module
from day20food import Food  # Import the Food class from day20food module
from day20scoreboard import Scoreboard  # Import the Scoreboard class from day20scoreboard module
import time  # Import the time module to control the speed of the game

# Set up the screen
screen = Screen()  # Create a screen object
screen.setup(width=600, height=600)  # Set the screen size to 600x600 pixels
screen.bgcolor("black")  # Set the background color of the screen to black
screen.title("This is Snake Game")  # Set the title of the window to "This is Snake Game"
screen.tracer(0)  # Turn off the screen updates for smoother animation

# Create the snake, food, and scoreboard objects
snake = Snake()  # Create a snake object
food = Food()  # Create a food object
scoreboard = Scoreboard()  # Create a scoreboard object

# Set up the keybindings for snake movement
screen.listen()  # Make the screen listen for key presses
screen.onkey(snake.up, "Up")  # Move the snake up when the "Up" key is pressed
screen.onkey(snake.down, "Down")  # Move the snake down when the "Down" key is pressed
screen.onkey(snake.left, "Left")  # Move the snake left when the "Left" key is pressed
screen.onkey(snake.right, "Right")  # Move the snake right when the "Right" key is pressed

# Main game loop
game_is_on = True  # A flag to keep the game running
while game_is_on:
    screen.update()  # Update the screen with the latest changes
    time.sleep(0.2)  # Pause the game for a short time to control the speed

    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random location
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()  # Increase the score

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
            snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_is_on = False  # End the game if the snake hits the wall
        scoreboard.game_over()  # Display "Game Over" message

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False  # End the game if the snake hits its own tail
            scoreboard.game_over()  # Display "Game Over" message

screen.exitonclick()  # Close the window when it is clicked


#slices in pyhon 
"""piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[1:5])"""



