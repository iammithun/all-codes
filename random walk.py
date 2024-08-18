# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:50:09 2024

@author: iamrs
"""

import turtle as t
import random

tim = t.Turtle()
tim.shape("square")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(2000000):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

