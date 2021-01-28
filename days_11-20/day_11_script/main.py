from random import randint

TO_GUESS = randint(1, 100)
HIGH = "Too high. \nGuess again.\n---------------"
LOW = "Too low. \nGuess again.\n---------------"
LIVES = 0


def set_difficulty():
    global LIVES
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        LIVES = 10
    elif difficulty == 'hard':
        LIVES = 5
    return LIVES


def check(user_input):
    if user_input > TO_GUESS:
        return HIGH
    elif user_input < TO_GUESS:
        return LOW
    else:
        return 1


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    global LIVES
    LIVES = set_difficulty()
    while LIVES > 0:
        print(f"You have {LIVES} attempts remaining to guess the number.")
        user_input = int(input("Make a guess :"))
        if check(user_input) == 1:
            print(f"You got it right! The answer was {user_input}")
            break
        else:
            LIVES = LIVES - 1
            if LIVES == 0:
                print("---------------\nYou've run out of guesses, you lose.")
                print(f"The answer was {TO_GUESS}")
            else:
                print(check(user_input))


game()
