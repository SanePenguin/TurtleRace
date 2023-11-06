from turtle import Turtle, Screen
import random

is_race_running = False

screen = Screen()
screen.setup(width=500, height=500)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in COLORS:
    tur = Turtle("turtle")
    tur.color(i)
    tur.penup()
    turtles.append(tur)
    tur.goto(x=-230, y=-100 + (len(turtles) * 33))

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

if user_bet:
    is_race_running = True
else:
    print("Please enter a color.")

while is_race_running:
    for turtle in turtles:
        random_distance = random.randint(1, random.randint(1, random.randint(1, 30)))
        if turtle.xcor() > 230:
            is_race_running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.strip().lower()[0]:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost. {winning_color} turtle made the race.")
        turtle.forward(random_distance)

screen.exitonclick()
