from turtle import Screen, Turtle
from day21paddle import Paddle
from day21ball import Ball
from day21scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()  # Create a screen object
screen.bgcolor("black")  # Set the background color to black
screen.setup(width=750, height=600)  # Set the size of the screen
screen.title("Pong")  # Set the title of the window
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))  # Create the right paddle and set its position
l_paddle = Paddle((-350, 0))  # Create the left paddle and set its position
ball = Ball()  # Create the ball
scoreboard = Scoreboard()  # Create the scoreboard

# Set up key listeners
screen.listen()  # Listen for key presses
screen.onkey(r_paddle.go_up, "Up")  # Move the right paddle up when the "Up" key is pressed
screen.onkey(r_paddle.go_down, "Down")  # Move the right paddle down when the "Down" key is pressed
screen.onkey(l_paddle.go_up, "w")  # Move the left paddle up when the "w" key is pressed
screen.onkey(l_paddle.go_down, "s")  # Move the left paddle down when the "s" key is pressed

game_is_on = True  # Flag to keep the game running
misses = 0  # Counter for missed balls

while game_is_on:  # Main game loop
    screen.update()  # Update the screen
    ball.move()  # Move the ball

    # Detect collision with wall and bounce the ball
    if ball.ycor() > 280 or ball.ycor() < -280:  # If the ball hits the top or bottom edge
        ball.bounce_y()  # Bounce the ball vertically

    # Detect collision with paddles and bounce the ball
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):  # If the ball hits a paddle
        ball.bounce_x()  # Bounce the ball horizontally

    # Detect if the right paddle misses the ball and update the score
    if ball.xcor() > 380:  # If the ball goes past the right paddle
        ball.reset_position()  # Reset the ball's position
        scoreboard.l_point()  # Increment the left paddle's score
        misses += 1  # Increment the miss counter

    # Detect if the left paddle misses the ball and update the score
    if ball.xcor() < -380:  # If the ball goes past the left paddle
        ball.reset_position()  # Reset the ball's position
        scoreboard.r_point()  # Increment the right paddle's score
        misses += 1  # Increment the miss counter

    # Check if there have been more than 10 misses
    if misses >= 10:  # If either paddle has missed the ball more than 10 times
        scoreboard.game_over()  # Display "Game Over" message
        game_is_on = False  # End the game

    time.sleep(ball.move_speed)  # Adjust game speed

screen.exitonclick()  # Close the window when clicked
