import turtle
import math

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("4D Tesseract Projection")

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Function to draw a line between two points
def draw_line(p1, p2):
    t.penup()
    t.goto(p1[0], p1[1])
    t.pendown()
    t.goto(p2[0], p2[1])

# Function to project 4D points to 3D
def project_4d_to_3d(point, angle):
    w, x, y, z = point
    distance = 2
    c = math.cos(angle)
    s = math.sin(angle)

    # Rotate in 4D space
    new_w = c * w - s * x
    new_x = s * w + c * x

    # Avoid division by zero
    if distance - new_w == 0:
        new_w += 0.0001

    # Perspective projection to 3D
    factor = distance / (distance - new_w)
    x3d = factor * new_x
    y3d = factor * y
    z3d = factor * z

    return [x3d, y3d, z3d]

# Function to project 3D points to 2D
def project_3d_to_2d(point):
    x, y, z = point
    distance = 2
    # Avoid division by zero
    if distance - z == 0:
        z += 0.0001
    factor = distance / (distance - z)
    x2d = factor * x * 100
    y2d = factor * y * 100
    return [x2d, y2d]

# Define vertices of a tesseract in 4D space
vertices_4d = [
    [-1, -1, -1, -1],
    [-1, -1, -1, 1],
    [-1, -1, 1, -1],
    [-1, -1, 1, 1],
    [-1, 1, -1, -1],
    [-1, 1, -1, 1],
    [-1, 1, 1, -1],
    [-1, 1, 1, 1],
    [1, -1, -1, -1],
    [1, -1, -1, 1],
    [1, -1, 1, -1],
    [1, -1, 1, 1],
    [1, 1, -1, -1],
    [1, 1, -1, 1],
    [1, 1, 1, -1],
    [1, 1, 1, 1]
]

# Edges connecting the vertices of a tesseract
edges = [
    (0, 1), (0, 2), (0, 4), (0, 8),
    (1, 3), (1, 5), (1, 9),
    (2, 3), (2, 6), (2, 10),
    (3, 7), (3, 11),
    (4, 5), (4, 6), (4, 12),
    (5, 7), (5, 13),
    (6, 7), (6, 14),
    (7, 15),
    (8, 9), (8, 10), (8, 12),
    (9, 11), (9, 13),
    (10, 11), (10, 14),
    (11, 15),
    (12, 13), (12, 14),
    (13, 15),
    (14, 15)
]

# Angle for 4D rotation
angle = 0

# Main loop to draw the tesseract
while True:
    t.clear()

    # Project 4D vertices to 3D and then to 2D
    projected_points = []
    for vertex in vertices_4d:
        point_3d = project_4d_to_3d(vertex, angle)
        point_2d = project_3d_to_2d(point_3d)
        projected_points.append(point_2d)

    # Draw edges
    for edge in edges:
        draw_line(projected_points[edge[0]], projected_points[edge[1]])

    # Update the screen
    screen.update()

    # Increment the angle
    angle += 0.01

# Keep the window open
turtle.done()
