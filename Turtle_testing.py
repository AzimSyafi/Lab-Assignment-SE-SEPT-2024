import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Pattern")

# Create a turtle object
spiral = turtle.Turtle()
spiral.speed(0)  # Set speed to the fastest

# List of colors to choose from
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "sayian"]

# Draw the spiral
for i in range(100):  # Number of loops for the spiral
    spiral.color(random.choice(colors))  # Pick a random color
    spiral.width(i / 25 + 1)  # Gradually increase the width
    spiral.forward(i * 2)  # Increase the distance forward
    spiral.left(59)  # Turn left to create the spiral effect

# Hide the turtle and display the window
spiral.hideturtle()
turtle.done()
