# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:52:37 2024

@author: iamrs
"""

from turtle import Turtle, Screen

# Function to draw a semi-circle of a specific color and radius
def draw_semi_circle(turtle, radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius, 180)
    turtle.end_fill()

# Initialize screen and turtle
screen = Screen()
screen.bgcolor("black")
screen.title("Rainbow")
screen.setup(width=600, height=600)

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
radius = 300
pen = Turtle()
pen.speed(0)
pen.width(20)

# Draw the rainbow
for color in rainbow_colors:
    draw_semi_circle(pen, radius, color)
    radius -= 20

pen.hideturtle()
screen.mainloop()
