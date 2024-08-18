# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:53:49 2024

@author: iamrs
"""

import turtle
import time

class Satellite:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = (0, 0)  # Initial position in space
        self.screen = turtle.Screen()
        self.screen.title("Satellite Movement")
        self.screen.setup(width=800, height=600)
        self.screen.tracer(0)
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.penup()
        self.pen.color(color)
        self.pen.shape("circle")
        self.pen.shapesize(0.5)
        self.pen.goto(self.position)
        self.pen.pendown()

    def move_to_mars(self):
        print(f"Sending satellite {self.name} to Mars...")
        self.pen.write(f"Sending satellite {self.name} to Mars...", align="center", font=("Arial", 12, "normal"))
        time.sleep(1)  # Simulating travel time
        for _ in range(180):
            self.position = self.calculate_new_position()
            self.pen.goto(self.position)
            self.screen.update()
            time.sleep(0.01)
        self.pen.clear()
        self.pen.write(f"Satellite {self.name} has reached Mars!", align="center", font=("Arial", 12, "normal"))

    def calculate_new_position(self):
        # Simulate elliptical orbit from Earth to Mars
        # For simplicity, using linear interpolation
        x = (1 - (_ / 180)) * 400 + (_ / 180) * 600
        y = (1 - (_ / 180)) * 0 + (_ / 180) * 100
        return x, y

# Create Earth and Mars
earth = turtle.Turtle()
earth.speed(0)
earth.color("blue")
earth.shape("circle")
earth.shapesize(5)
earth.penup()
earth.goto(0, 0)

mars = turtle.Turtle()
mars.speed(0)
mars.color("red")
mars.shape("circle")
mars.shapesize(3)
mars.penup()
mars.goto(600, 100)

# Create a satellite object
mars_satellite = Satellite("MarsSatellite1", "green")

# Send the satellite to Mars
mars_satellite.move_to_mars()

# Keep the window open
mars_satellite.screen.mainloop()
