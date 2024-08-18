import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.pensize(2)

# Draw the apple
def draw_apple():
    pen.begin_fill()

    # Draw the bottom of the apple
    pen.circle(100, 180)
    pen.circle(50, 180)

    # Draw the body of the apple
    pen.forward(10)
    pen.circle(40, 180)
    pen.circle(80, 180)
    pen.circle(40, 180)
    pen.forward(10)

    # Draw the top of the apple
    pen.circle(50, 180)
    pen.circle(100, 180)
    pen.end_fill()

    # Draw the apple stem
    pen.up()
    pen.goto(0, 200)
    pen.down()
    pen.color("green")
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

draw_apple()

# Hide the Turtle
pen.hideturtle()

# Keep the window open
turtle.mainloop()
