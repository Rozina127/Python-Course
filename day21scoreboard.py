from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()  # Initialize the Turtle class
        self.color("white")  # Set the color of the text to white
        self.penup()  # Lift the pen to prevent drawing lines
        self.hideturtle()  # Hide the turtle icon
        self.l_score = 0  # Initialize the left paddle's score
        self.r_score = 0  # Initialize the right paddle's score
        self.update_scoreboard()  # Display the initial scores

    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.goto(-100, 200)  # Move to the left score position
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # Display the left score
        self.goto(100, 200)  # Move to the right score position
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # Display the right score

    def l_point(self):
        self.l_score += 1  # Increment the left score
        self.update_scoreboard()  # Update the scoreboard

    def r_point(self):
        self.r_score += 1  # Increment the right score
        self.update_scoreboard()  # Update the scoreboard

    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER\nTRY AGAIN", align="center", font=("Courier", 40, "normal"))  # Display "Game Over" message
