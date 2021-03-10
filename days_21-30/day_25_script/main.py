# Miles to Kilometer
# Imports
import tkinter

# Window settings

window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=70)
window.config(padx=10, pady=10)

# Labels
miles = tkinter.Label(text="Miles", font=("Arial", 18))
is_equal_to = tkinter.Label(text="Is equal to: ", font=("Arial", 18))
km = tkinter.Label(text="Km", font=("Arial", 18))
value = tkinter.Label(text="0", font=("Arial", 18))

# Input
user_input = tkinter.Entry(width=10)


# Button
def buttonClick():
    value_to_calculate = float(user_input.get())
    calculated = round(value_to_calculate * 1.609344,2)
    value.config(text=calculated)


calculate = tkinter.Button(text="Calculate",font=("Arial", 18), command=buttonClick)

# Positions
user_input.grid(column=1, row=0)
miles.grid(column=2, row=0)
is_equal_to.grid(column=0, row=1)
value.grid(column=1, row=1)
km.grid(column=2, row=1)

calculate.grid(column=1, row=2)

window.mainloop()
