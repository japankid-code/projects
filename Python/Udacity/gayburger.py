import turtle
rainbows = ["red", "orange", "yellow", "green", "blue", "purple"]
terry = turtle.Turtle()
terry.width(10)
# Write whatever code you want here!
terry.back(50)
terry.speed(0)
for rainbow in rainbows:
    terry.color(rainbow)
    terry.forward(50)
    terry.penup()
    terry.right(90)
    terry.forward(10)
    terry.right(90)
    terry.forward(50)
    terry.right(180)
    terry.pendown()

# this is for making colored stars around the rainbow
terry.penup()
terry.left(90)
terry.forward(110)
terry.width(5)
terry.right(90)
terry.forward(5)
terry.left(20)
stars = [1, 2, 3, 4, 5, 6]
for rainbow in rainbows:
    terry.color(rainbow)
    terry.pendown()
    for star in stars:
        terry.forward(40)
        terry.right(144)
    terry.penup()
    terry.left(85)
    terry.forward(50)
