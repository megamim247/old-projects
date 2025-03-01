from turtle import Screen, Turtle, Vec2D
from random import uniform, choice
from math import pi, cos, sin

def is_point_inside_shape(x, y, vertices):
    # Use ray-casting algorithm to check if point is inside the shape

    num_intersections = 0

    for index, p1 in enumerate(vertices):
        p2 = vertices[(index+1) % len(vertices)]

        if p1[1] <= y < p2[1] or p2[1] <= y < p1[1]:
            p3 = p2 - p1

            if x < p3[0] * (y - p1[1]) / p3[1] + p1[0]:
                num_intersections += 1

    return num_intersections % 2 == 1

def add_points(num_sides, side_length, iterations, distance, speed):
    turtle.speed(speed)

    # Create vertices
    vertices = []
    angle = pi*2 / num_sides

    for i in range(num_sides):
        x = side_length * cos(angle * i)
        y = side_length * sin(angle * i)
        vertices.append(Vec2D(x, y))

    # Draw the outline of the shape
    turtle.penup()

    for vertex in vertices:
        turtle.goto(vertex)
        turtle.pendown()

    turtle.goto(vertices[0])
    turtle.penup()

    # Draw a random point inside the shape

    while True:
        x, y = uniform(-side_length/2, side_length/2), uniform(-side_length/2, side_length/2)

        if is_point_inside_shape(x, y, vertices):
            # Draw the point and break the loop
            turtle.goto(x, y)
            turtle.dot(4, 'red')
            break

    # Iterate and draw points

    for _ in range(iterations):
        # Calculate the distance between the current position and the chosen vertex
        delta = (choice(vertices) - turtle.position()) * distance

        # Move the turtle to the new position
        turtle.goto(turtle.position() + delta)

        # Draw a dot at the new position
        turtle.dot(2, 'blue')

    # Done drawing
    turtle.penup()

screen = Screen()

# Set up the turtle
turtle = Turtle()
turtle.hideturtle()

# add_points(num_sides, side_length, num_points, distance from vertex, speed)
add_points(3, 250, 10000, 1/2, 'fastest')