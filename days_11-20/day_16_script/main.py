import colorgram
import turtle as t
import random

list_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    list_colors.append(new_color)


t.colormode(255)
drawing_guy = t.Turtle()
drawing_guy.hideturtle()
drawing_guy.speed("fastest")
drawing_guy.penup()
drawing_guy.setheading(255)
drawing_guy.forward(300)
drawing_guy.setheading(0)
dots = 100


for i in range(1, dots + 1):
    drawing_guy.dot(20, random.choice(list_colors))
    drawing_guy.forward(50)

    if i % 10 == 0:
        drawing_guy.setheading(90)
        drawing_guy.forward(50)
        drawing_guy.setheading(180)
        drawing_guy.forward(500)
        drawing_guy.setheading(0)




screen = t.Screen()
screen.exitonclick()