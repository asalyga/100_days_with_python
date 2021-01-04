from turtle import Turtle, Screen
import random
race = False
start_y = -100
start_x = -280
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Bet", prompt="Who's gonna be the winner? Enter a color: ")
colors = ["red", "orange", "blue", "yellow", "green", "purple"]
turtles = []
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=start_x, y=start_y)
    turtle.pendown()
    start_y += 30
    turtles.append(turtle)

if user_bet:
    race = True


while race:
    for turtle in turtles:
        if turtle.xcor() > 260:
            race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations, {winning_color} wins!")
            else:
                print(f"You lose! {winning_color} wins!")
        dis = random.randint(0, 10)
        turtle.forward(dis)


screen.exitonclick()
