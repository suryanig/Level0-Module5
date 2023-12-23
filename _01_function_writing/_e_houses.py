"""
Have the turtle draw a row of houses.
"""
import random
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    window = Tk()
    window.withdraw()
    turtle = turtle.Turtle()
    turtle.penup()
    turtle.goto(-465,-375)
    turtle.pendown()
    turtle.pencolor('green')
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    turtle.forward(920)
    turtle.penup()
    turtle.goto(-465,-373)
    turtle.pendown()

    def draw_house(size):
        height = random.randint(60,250)
        if size == "small":
            height = 60
        elif size == "medium":
            height = 120
        elif size == "large":
            height = 250
        turtle.pencolor('black')
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
        turtle.forward(92)

    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    def draw_pointy_roof():
        turtle.left(45)
        turtle.forward(63)
        turtle.right(90)
        turtle.forward(63)

    def draw_flat_roof():
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(10)

    for i in range (10):
        r = random.randint(1,3)
        if r == 1:
            draw_house("small")
            turtle.penup()
            turtle.goto(-465+90*i,-313)
            turtle.pendown()
            draw_pointy_roof()
            turtle.penup()
            turtle.goto(-465+90*i+90,-373)
            turtle.pendown()
            turtle.left(45)
        elif r == 2:
            draw_house("medium")
            turtle.penup()
            turtle.goto(-465+90*i,-253)
            turtle.pendown()
            draw_pointy_roof()
            turtle.penup()
            turtle.goto(-465+90*i+90,-373)
            turtle.pendown()
            turtle.left(45)
        elif r == 3:
            draw_house("large")
            turtle.penup()
            turtle.goto(-465+90*i,-123)
            turtle.pendown()
            draw_flat_roof()
            turtle.penup()
            turtle.goto(-465+90*i+90,-373)
            turtle.pendown()
            turtle.left(90)
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof


    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    window.mainloop()
    pass
