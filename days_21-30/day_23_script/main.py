import pandas as pd
import turtle
game_on = True
guessed = []
screen = turtle.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()


while len(guessed) < 50:
    usr_answer = screen.textinput(title=f"{len(guessed)}/50 Guess the state",
                                  prompt="What's another state's name?").title()
    if usr_answer == "Exit":
        missed = []
        for state in states:
            if state not in guessed:
                missed.append(state)

        new_data = pd.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        break
    if usr_answer in states:
        guessed.append(usr_answer)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        state_data = data[data.state == usr_answer]
        tur.goto(int(state_data.x), int(state_data.y))
        tur.write(state_data.state.item())

