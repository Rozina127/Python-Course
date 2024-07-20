import random
from hangman_words import word_list
from hangman_art import logo, stages

# Select a random word from the word list
target_word = random.choice(word_list)
word_length = len(target_word)

# Initialize game variables
game_over = False
remaining_lives = 6

# Display the hangman logo
print(logo)

# Create a list to show the current state of the word
current_display = ['_'] * word_length

while not game_over:
    # Get user input
    guessed_letter = input("Guess a letter: ").lower()

    # Check if the user has already guessed this letter
    if guessed_letter in current_display:
        print(f"You've already guessed '{guessed_letter}'")
        continue
    
    # Update the display with the guessed letter
    if guessed_letter in target_word:
        for index in range(word_length):
            if target_word[index] == guessed_letter:
                current_display[index] = guessed_letter
    else:
        print(f"'{guessed_letter}' is not in the word. You lose a life.")
        remaining_lives -= 1
        if remaining_lives == 0:
            game_over = True
            print("You lose.")
    
    # Print the current state of the word
    print(' '.join(current_display))
    
    # Print the current hangman stage
    print(stages[remaining_lives])

    # Check if the user has guessed all the letters
    if "_" not in current_display:
        game_over = True
        print("You win.")
