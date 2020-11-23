import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img = [rock, paper, scissors]
user = int(input("What do you choose? (Type '0' for rock, '1' for paper, '2' for Scissors) : "))
print(game_img[user])

computer = random.randint(0, 2)


print(f"computer choose:")
print(game_img[computer])


if user >= 3 or user < 0:
    print("You typed invalid number!")
elif user == 0 and computer == 2:
    print("User wins!")
elif computer == 0 and user == 2:
    print("Computer wins!")
elif computer > user:
    print("Computer wins!")
elif user > computer:
    print("User wins!")
elif computer == user:
    print("Its a draw!")


