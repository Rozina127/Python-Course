import random

# Function to return a random card from the deck
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate the score of a given list of cards
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards."""
    # Check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check if the score is over 21 and if there's an 11 (ace), convert the 11 to a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare the scores of the user and the computer
def compare(user_score, computer_score):
    """Compare the user's score with the computer's score and return the result."""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Main function to play the game
def play_game():
    # Initialize the user and computer's cards
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal 2 cards to each player
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Continue the game until it's over
    while not is_game_over:
        # Calculate the scores for both players
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        # Check if the game is over (blackjack or score over 21)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn to draw cards until its score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show the final hands and scores
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    # Compare the final scores and print the result
    print(compare(user_score, computer_score))

# Start a new game if the user wants to play again
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
