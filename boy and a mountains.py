import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Mountain Scene with a Boy")
screen.bgcolor("sky blue")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)

def draw_mountain(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.goto(x + width / 2, y + height)
    t.goto(x + width, y)
    t.goto(x, y)
    t.end_fill()

def draw_sun(x, y, radius):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_boy(x, y):
    # Draw head
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("peach puff")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Draw body
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y - 20)
    
    # Draw arms
    t.goto(x - 15, y - 10)
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.goto(x + 15, y - 10)
    
    # Draw legs
    t.goto(x, y - 20)
    t.goto(x - 10, y - 40)
    t.penup()
    t.goto(x, y - 20)
    t.pendown()
    t.goto(x + 10, y - 40)

# Draw mountains
draw_mountain(-200, -100, 400, 300, "dark green")
draw_mountain(-100, -100, 300, 200, "forest green")
draw_mountain(0, -100, 400, 300, "sea green")

# Draw sun
draw_sun(150, 150, 50)

# Draw boy
draw_boy(0, -50)

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
