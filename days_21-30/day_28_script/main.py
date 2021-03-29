import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip3
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
               'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0, tk.END)
    input_password.insert(0, password)
    pyperclip3.copy(password)


# ---------------------------- SAVE PASSWORD -------------------------------- #
def save_password():
    website = input_website.get()
    password = input_password.get()
    email = input_email_user.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 \
            or len(password) == 0 \
            or len(email) == 0:
        messagebox.showerror(title="Error",
                             message="Please do not leave any fields empty!")
    else:
        try:
            with open("saved_passwords.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("saved_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("saved_passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            input_website.delete(0, tk.END)
            input_email_user.delete(0, tk.END)
            input_password.delete(0, tk.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = input_website.get()

    try:
        with open("saved_passwords.json", "r") as json_data:
            data = json.load(json_data)
    except FileNotFoundError:
        messagebox.showerror(title="Error",
                             message="You don't have any passwords saved")
    else:
        with open("saved_passwords.json", "r") as json_data:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showerror(title="Result",
                                     message=f"Website: {website} \n"
                                             f"Email: {email} \n"
                                             f"Password: {password}")
            else:
                messagebox.showerror(title="Error",
                                     message=f"No details for {website} exist")


# ---------------------------- UI SETUP -------------------------------------- #
# TODO: Setup window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# TODO: Setup a canvas with "logo" img
canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
# TODO: Setup the labels and input fields and buttons

# Labels
label_website = tk.Label(text="Website:")
label_email_user = tk.Label(text="Email/Username:")
label_password = tk.Label(text="Password: ", )
# Input fields
input_website = tk.Entry(width=21)
input_website.focus()
input_email_user = tk.Entry(width=35)
input_password = tk.Entry(width=21, show="*")

# Buttons
button_generate_pw = tk.Button(text="Generate Password", command=pass_gen)
button_add = tk.Button(text="Add", width=36, command=save_password)
button_search = tk.Button(text="Search", width=13, command=search_password)

# TODO: GRID LAYOUT

canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
input_website.grid(column=1, row=1)

label_email_user.grid(column=0, row=2)
input_email_user.grid(column=1, row=2, columnspan=2)

label_password.grid(column=0, row=3)
input_password.grid(column=1, row=3)

button_generate_pw.grid(column=2, row=3)
button_add.grid(column=1, row=4, columnspan=2)
button_search.grid(column=2, row=1)

# Main loop
window.mainloop()
