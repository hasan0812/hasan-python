import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create flower
petals = turtle.Turtle()
petals.speed(0)
petals.width(3)

# Draw petals
for i in range(12):
    petals.color("pink") if i % 2 == 0 else petals.color("purple")
    petals.circle(50)
    petals.left(30)

# Draw center
center = turtle.Turtle()
center.dot(30, "yellow")

# Draw stem
stem = turtle.Turtle()
stem.color("green")
stem.width(5)
stem.right(90)
stem.penup()
stem.goto(0, -50)
stem.pendown()
stem.forward(150)

# Draw leaf
leaf = turtle.Turtle()
leaf.color("green")
leaf.width(3)
leaf.penup()
leaf.goto(0, -100)
leaf.pendown()
leaf.begin_fill()
leaf.circle(40, 70)
leaf.left(110)
leaf.circle(40, 70)
leaf.end_fill()

turtle.done