import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

# Create blanks
display = ['_'] * word_length

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # If the user has entered a letter they've already guessed
    if guess in display:
        print(f"You've already guessed {guess}")
        continue  # Skip the rest of the loop if the letter was already guessed

    # Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    # Print the current state of the word
    print(f"{' '.join(display)}")
    
    # Print the hangman stage
    print(stages[lives])

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win.")
