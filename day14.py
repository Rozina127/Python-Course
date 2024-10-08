import random

from day14_gamedata import data  # The data containing the account information

def get_random_account():
  """Get data from a random account."""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description, and country."""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Check the user's guess against the follower counts and return True if the guess is correct, otherwise False."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  # Ensure that account_a and account_b are different at the start
  while account_a == account_b:
    account_b = get_random_account()

  while game_should_continue:
    account_a = account_b  # Move the current account_b to account_a
    account_b = get_random_account()

    # Ensure that the new account_b is different from account_a
    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

   
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
game()
