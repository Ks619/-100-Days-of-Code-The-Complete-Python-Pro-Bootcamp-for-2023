"""Turtle race - There is 6 turtles with different colors, the user bet on which turtle will win"""
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtles race - Make your bet",
                            prompt="Choose a color (red,blue,yellow,purple,green,orange): ")
turtles = []
colors = ["red", "blue", "yellow", "purple", "green", "orange"]
location = -145
race_on = False
for index in range(6):
    new_turtle = Turtle()
    turtles.append(new_turtle)
    turtles[index].color(colors[index])
    turtles[index].shape("turtle")
    turtles[index].setheading(0)  # loge mode
    turtles[index].penup()
    turtles[index].setpos(-230, location)
    location += 60

if user_bet:
    race_on = True

while race_on:

    for turtle in turtles:
        if turtle.xcor() >= 230:
            race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")
            break

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
