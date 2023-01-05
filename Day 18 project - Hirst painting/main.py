"""Paints a square builds from dots (size:20), between each dot there is a space (size:50),
    the length of each side is 10 dots.All the colors of the dots extracts from image.jpg
     using the colorgram package."""

import random
import colorgram
import turtle as turtle_module

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

turtle_module.colormode(255)
paint = turtle_module.Turtle()

paint.speed("fastest")
paint.hideturtle()

for index in range(10):
    paint.penup()
    paint.setposition(-235, index * 50 - 220)
    for index1 in range(10):
        paint.pendown()
        paint.dot(20, random.choice(rgb_colors))
        paint.penup()
        paint.forward(50)

screen = turtle_module.Screen()
screen.exitonclick()
