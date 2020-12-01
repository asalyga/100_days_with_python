# caesar Cipher
import day_7_assets

on = True


def caesar(user_option, user_message, shift_amount):
    the_message = ""
    if user_option == "decode":
        shift_amount *= -1
    for char in user_message:
        if char in day_7_assets.alphabet:
            the_message += day_7_assets.alphabet[day_7_assets.alphabet.index(char) + shift_amount]
        else:
            the_message += char
    print(f"The {user_option} is {the_message}")


print(day_7_assets.logo)
print("This is Caesar Cipher")

while on:
    option = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = list(input("Type your message:\n"))
    shift = int(input("Please type the shift number:\n"))
    caesar(user_option=option, user_message=message, shift_amount=(shift%25))
    continue_work = input("Do you wanna start again?: (Type 'yes' or 'no')\n ").lower()
    if continue_work == 'no':
        on = False
        print("Goodbye")
