from random import randint

# Number of turns for easy and hard levels
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Check the user's guess against the actual answer and return the number of turns remaining."""
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}.")
        return turns  # No change to turns if the guess is correct
    return turns - 1  # Reduce turns if the guess is wrong

def set_difficulty():
    """Ask the user to choose a difficulty level and return the number of turns based on the choice."""
    level = input("Choose a difficulty level: 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    """Main function to run the number guessing game."""
    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")  # For debugging; remove or comment out in production

    # Set the number of turns based on the chosen difficulty
    turns = set_difficulty()
    
    guess = 0  # Initialize guess variable
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        
        # Ask the user to make a guess
        guess = int(input("Make a guess: "))
        
        # Check the guess and update the number of turns
        turns = check_answer(guess, answer, turns)
        
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again.")

# Start the game
game()
