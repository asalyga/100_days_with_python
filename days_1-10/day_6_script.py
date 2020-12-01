import random,day_6_assets
game = True
lives = 6
chosen_word = random.choice(day_6_assets.word_list)
display = ["_" for i in chosen_word]
print("Welcome to hangman")
print(day_6_assets.logo)
print(display)
while game:
    guess = input("Your letter: ").lower()
    if guess in chosen_word:
        for i in range(len(display)):
            if chosen_word[i] == guess:
                display[i] = guess
        print()
    if guess in display:
        print("You already choosen this letter")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("Game Over")
            game = False

    if display == list(chosen_word):
        print("You win!")
        game = False

    print(day_6_assets.stages[lives])