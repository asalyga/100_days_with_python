from day_12_assets import logo,vs, data
import random, os
def clear_screen():
    os.system('cls||clear')

score = 0
game_on = True
account_b = random.choice(data)

def format_data(account):
    """Formatting the account data """
    return (f"{account['name']}, a {account['description']}, from {account['country']}.")


### Use If statement to check if user is correct.
def check_answer(user_input, follower_count_a, follower_count_b):
    """Takes user guess and accounts and returns if they got it right"""
    if follower_count_a > follower_count_b:
        return user_input == 'a'
    else:
        return user_input == 'b'


# Display art
print(logo)

while game_on:
    # Generate a random accout from data game
    # Make account at position B become next account as position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    # Format account data into printable format
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    # Ask user for a guess
    user_answer = input("Who has more followers? Type 'A' or 'B' :").lower()


    # Check if user is correct.
    ## Get follower count of each account
    follower_count_a = account_a['follower_count']
    follower_count_b = account_b['follower_count']

    is_correct = check_answer(user_answer, follower_count_a, follower_count_b)

    # Clear screen 
    clear_screen()
    print(logo)

    # Give user feedback on the guess
    ## Keep score
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_on = False
        print(f"Sorry, that's the wrong answer. Final score {score}.")





            