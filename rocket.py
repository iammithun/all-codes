import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Rocket Launch with Satellite")

# Create the rocket
rocket = turtle.Turtle()
rocket.shape("square")
rocket.color("blue")
rocket.shapesize(stretch_wid=1, stretch_len=3)

# Create the fire
fire = turtle.Turtle()
fire.shape("triangle")
fire.color("orange")
fire.shapesize(stretch_wid=1, stretch_len=1.5)
fire.penup()
fire.goto(rocket.xcor(), rocket.ycor() - 35)
fire.setheading(270)

# Create the satellite
satellite = turtle.Turtle()
satellite.shape("circle")
satellite.color("white")
satellite.shapesize(stretch_wid=0.5, stretch_len=0.5)
satellite.penup()
satellite.hideturtle()

# Function to launch the rocket
def launch_rocket():
    rocket.penup()
    fire.penup()
    y = rocket.ycor()
    for _ in range(30):
        y += 10
        rocket.sety(y)
        fire.sety(y - 35)
        time.sleep(0.1)
    fire.hideturtle()

# Function to deploy the satellite
def deploy_satellite():
    satellite.goto(rocket.xcor(), rocket.ycor() + 30)
    satellite.showturtle()
    for _ in range(36):
        satellite.circle(30, 10)
        time.sleep(0.1)

# Run the launch sequence
launch_rocket()
deploy_satellite()

# End program
turtle.done()
