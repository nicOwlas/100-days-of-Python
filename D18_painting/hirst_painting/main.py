import turtle as t
import random

t.colormode(255)
turtle = t.Turtle()
turtle.speed('fastest')
turtle.hideturtle()

color_list = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), (179, 17, 8), (233, 66, 34)]

turtle.penup()
turtle.setpos(-250,-250)
for column in range(10):
    for row in range(10):
        turtle.pendown()
        turtle.dot(20,random.choice(color_list))
        turtle.penup()
        turtle.forward(50)
    turtle.backward(500)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()


# # Extract 6 colors from an image.
# colors = colorgram.extract('palette.jpg', 30)

# palette = []

# for color in colors:
#     palette.append(tuple(color.rgb))

# print(palette)

# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s