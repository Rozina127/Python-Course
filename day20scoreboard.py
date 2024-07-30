from turtle import Turtle  # Import Turtle class from the turtle module

# Constants for text alignment and font style
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0  # Initialize the score
        self.color("white")  # Set the text color
        self.penup()  # Lift the pen to avoid drawing lines
        self.hideturtle()  # Hide the turtle icon
        self.goto(0, 260)  # Position the scoreboard at the top of the screen
        self.update_scoreboard()  # Display the initial score

    def update_scoreboard(self):
        self.clear()  # Clear the previous score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Display the current score

    def increase_score(self):
        self.score += 1  # Increase the score
        self.update_scoreboard()  # Update the displayed score

    def game_over(self):
        self.goto(0, 0)  # Move to the center of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Display "GAME OVER" message
        self.goto(0, -30)  # Move slightly below the "GAME OVER" message
        self.write("TRY AGAIN", align=ALIGNMENT, font=FONT)  # Display "TRY AGAIN" msg
