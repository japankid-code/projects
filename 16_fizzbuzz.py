import turtle

def fizz(tur):
    # A red square bead.
    tur.color("red")
    tur.left(90)
    for side in [10, 20, 20, 20, 10]:
        tur.forward(side)
        tur.right(90)

def buzz(tur):
    # A green hexagonal bead.
    # Fits inside the red bead.
    tur.color("green")
    tur.left(60)
    for side in range(6):
        tur.forward(10)
        tur.right(60)
    tur.right(60)

def plain(tur):
    # A gray octagonal bead.
    tur.color("gray")
    tur.left(90)
    for side in [4, 8, 8, 8, 8, 8, 8, 8, 4]:
        tur.forward(side)
        tur.right(45)
    tur.right(45)

# Set up the turtle to draw beads.
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()
t.back(180)  # Back up to make room!
t.pendown()

for num in range(16):
    # Change this code:
    if num % 3 == 0:
        # draws the red sq bead on the if div by 3 w/o remainder
        fizz(t)
        if num % 5 == 0:
            # draws the green bead if div by 5 and 3 w/o remainder :)
            buzz(t)
    else:
        if num % 5 == 0:
            # draws  the green bead if num is only div by 5 w/o remainder
            buzz(t)
        else:
            # draws the plain bead on other spots
            plain(t)
    # Advance to the next bead spot.
    t.forward(22)
t.hideturtle()
