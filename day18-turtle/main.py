import turtle as t
import random
import colorgram
# from turtle import * -- imports errthang, not commonly used
# aliasing modules
    # import turtle as t
    # turtle = t.Turtle()
# install packages
# pip install [package]
# pypi.org

turtle = t.Turtle()

# turtle.shape("turtle")
# turtle.color("red")
# square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# dashed line
# for _ in range(6):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# shapes challenge

# colors = ["CornflowerBlue", "DarkOrchid", "red", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# angles = [90, -90]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         turtle.forward(100)
#         turtle.right(angle)

# for shape_side_n in range(3,10):
#     turtle.color(random.choice(colors)) # ooh pretty
#     draw_shape(shape_side_n)

# random walk challenge
# random color
# t.colormode(255)
# def random_color():
#     r= random.randint(0,255)
#     g= random.randint(0,255)
#     b= random.randint(0,255)
#     return (r,g,b)

# turtle.speed(10)
# turtle.pensize(10)
# def random_walk():
#     turtle.color(random_color())
#     turtle.right(random.choice(angles))
#     turtle.forward(30)

# for _ in range(50):
#     random_walk()

# Tuples
# (1, 3, 8)
# tuples are immutable
# list(my_tuple) -- converts a tuple to a list if needed

# hirst painting generator
t.colormode(255)
rgb_colors = [(240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72)]
# extract colors from image and convert to r,g,b tuples
# colors = colorgram.extract('image.jpg', 15)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

turtle.hideturtle()
turtle.penup()
turtle.setheading(225)
turtle.forward(100)
turtle.setheading(0)
turtle.speed("fastest")
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    turtle.dot(20, random.choice(rgb_colors))
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)



screen = t.Screen()
screen.exitonclick()