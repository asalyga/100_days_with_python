print("Email generator")
domain = input("Enter your email domain (for example: @gmail.com): ")
first_name = input("What's your first name? :")
last_name = input("What's your last name? :")
choice = input("Do you want your email to contain additional word? (y/n): ")
if choice == "y":
    add_word = input("Write additional word you want your email to contain: ")
    print(first_name[0:3].lower() + last_name[0:3].lower() + add_word.lower() + "@" + domain.lower() )
else:
    print(first_name[0:3].lower() + last_name[0:3].lower() + "@" + domain.lower() + ".com")

