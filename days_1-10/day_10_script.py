import day_10_assets
import random

print(day_10_assets.logo)
print("Welcome to the BLACKJACK GAME")
player_deck = []
computer_deck = []


def draw_card():
    return random.choice(day_10_assets.cards)


def calc_score(deck_to_calculate):
    score = sum(deck_to_calculate)
    if (deck_to_calculate[0] + deck_to_calculate[1]) == 21:
        score = 0
        return score
    else:
        return score


def result(player_score, comp_score):
    if player_score > 21 and comp_score > 21:
        return "Both went over, GAME OVER"

    if player_score == comp_score:
        return "It's a DRAW!"
    elif comp_score == 0:
        return "BLACKJACK, Computer wins!"
    elif player_score == 0:
        return "BLACKJACK, Player wins!"
    elif player_score > 21:
        return "You are over 21, Computer wins!"
    elif comp_score > 21:
        return "Computer is over 21, Player wins!"
    elif player_score > comp_score:
        return "Player wins!"
    else:
        return "Computer wins!"


def blackjack():
    for i in range(2):
        computer_deck.append(draw_card())
        player_deck.append(draw_card())

    comp_score = calc_score(computer_deck)

    player_game = True
    while player_game:
        player_score = calc_score(player_deck)
        print(f"Your cards: {player_deck}, Your score: {player_score}\nComputer first card: {computer_deck[0]}")
        print("-------------------------------------------------------------------------")
        if player_score == 0 or comp_score == 0 or player_score > 21:
            player_game = False
        else:
            to_play = input("Do you wanna draw a card? (type 'y' if yes or 'n' if no) : ").lower()
            if to_play == "y":
                player_deck.append(draw_card())
            else:
                player_game = False

    while comp_score < 17:
        computer_deck.append(draw_card())
        comp_score = calc_score(computer_deck)

    print(f"Your score is {player_score}\nComputer score is {comp_score}")
    print("---------------------------------------------------------------")

    print(result(player_score, comp_score))


blackjack()
