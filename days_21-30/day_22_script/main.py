# Mail Merge script

with open("input/Letters/starting_letter.txt", mode='r') as letter:
    starting_letter = letter.read()

with open("input/Names/invited_names.txt") as names:
    for name in names:
        name = name.strip()
        letter = starting_letter.replace("[name]", name)
        with open(f"output/ReadyToSend/{name}.txt", mode='w') as done:
            done.write(letter)
