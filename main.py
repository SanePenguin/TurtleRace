from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=500)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in COLORS:
    tur = Turtle("turtle")
    tur.color(i)
    tur.penup()
    turtles.append(tur)
    tur.goto(x=-230, y=-180 + (len(turtles) * 60))

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

screen.exitonclick()
