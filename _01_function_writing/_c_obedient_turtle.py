"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    turtle = turtle.Turtle()
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    def square ():
        turtle.pendown()
        for i in range(4):
            turtle.forward(300)
            turtle.right(90)
    def triangle():
        turtle.pendown()
        for i in range (3):
            turtle.forward(300)
            turtle.right(120)
    def circle():
        turtle.pendown()
        turtle.circle(150)
    #   3. Ask the user for the for a shape to draw.
    shape = simpledialog.askstring(title='Shape', prompt="What shape do you want me to draw?")
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if shape == "square":
        square()
    elif shape == "triangle":
        triangle()
    elif shape == "circle":
        circle()
    pass
