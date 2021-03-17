import tkinter as tk
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip3


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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(input_website.get()) == 0 \
            or len(input_password.get()) == 0 \
            or len(input_email_user.get()) == 0:
        messagebox.showerror(title="Error",
                             message="Please do not leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=input_website.get(),
                                       message=f"These are the details entered: "
                                               f"\n Email {input_email_user.get()}"
                                               f" \n Password {input_password.get()}")
        if is_ok:
            with open("saved_passwords.txt", "a") as data_file:
                data_file.write(f"{input_website.get()} | {input_email_user.get()} | {input_password.get()} \n")
                data_file.close()

            input_website.delete(0, tk.END)
            input_email_user.delete(0, tk.END)
            input_password.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
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
input_website = tk.Entry(width=35)
input_website.focus()
input_email_user = tk.Entry(width=35)
input_password = tk.Entry(width=21, show="*")

# Buttons
button_generate_pw = tk.Button(text="Generate Password", command=pass_gen)
button_add = tk.Button(text="Add", width=36, command=save_password)

# TODO: GRID LAYOUT

canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
input_website.grid(column=1, row=1, columnspan=2)

label_email_user.grid(column=0, row=2)
input_email_user.grid(column=1, row=2, columnspan=2)

label_password.grid(column=0, row=3)
input_password.grid(column=1, row=3)

button_generate_pw.grid(column=2, row=3)
button_add.grid(column=1, row=4, columnspan=2)

# Main loop
window.mainloop()
