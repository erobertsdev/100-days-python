from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# def move(key):
#     if key == 'w':
#         clem.forward(10)
#     elif key =='s':
#         clem.backward(10)

# screen.listen()
# screen.onkey(key="w", fun=move)

# Turtle race
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_pos = 100
for idx, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[idx])
    new_turtle.penup()
    new_turtle.goto(-230,y_pos)
    y_pos -= 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
    print(all_turtles)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! {winning_color} was the winning turtle!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# clem = Turtle(shape="turtle")
# clem.penup()
# clem.goto(-230,-100)

screen.exitonclick()