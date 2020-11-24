#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

the_password = []
password_string = ""
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for letter in range(0, nr_letters, 1):
    random_thing = random.choice(letters)
    the_password.append(letters[random_thing])
for number in range(0, nr_symbols, 1):
    random_thing = random.choice(numbers)
    the_password.append(numbers[random_thing])
for sign in range(0, nr_numbers, 1):
    random_thing = random.choice(symbols)
    the_password.append(symbols[random_thing])

random.shuffle(the_password)

password_string = ''.join([str(elem) for elem in the_password])

print(f"Your password is \n {password_string}")
