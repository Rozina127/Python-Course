# Import the necessary libraries
import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")  # Set the title of the screen

# Load the map image
image = "day25project_blank_states_img.gif"
screen.addshape(image)  # Add the image as a shape to the turtle screen
turtle.shape(image)  # Set the turtle shape to the map image

# Load state data
data = pandas.read_csv("day25project_50_states.csv")  # Read the CSV file containing state data
all_states = data.state.to_list()  # Convert the 'state' column to a list
guessed_states = []  # List to keep track of guessed states

# Main game loop
while len(guessed_states) < 50:
    # Prompt user for input
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # Check if user wants to exit
    if answer_state == "Exit":
        # Create a list of states that were not guessed
        missing_states = [state for state in all_states if state not in guessed_states]

        # Save missing states to a new CSV file
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("day25project_states_to_learn.csv")
        break

    # Check if the guessed state is correct
    if answer_state in all_states:
        guessed_states.append(answer_state)  # Add the guessed state to the list
        t = turtle.Turtle()  # Create a new turtle for writing the state name
        t.hideturtle()  # Hide the turtle icon
        t.penup()  # Lift the pen so it doesn't draw lines
        state_data = data[data.state == answer_state]  # Get the data for the guessed state
        t.goto(state_data.x.item(), state_data.y.item())  # Move the turtle to the state's coordinates
        t.write(answer_state)  # Write the state name at the correct coordinates
