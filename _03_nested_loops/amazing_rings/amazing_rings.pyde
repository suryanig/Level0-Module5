"""
Go to the recipe to run the demonstration before starting this program
"""
x=200
def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(800,400)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
def draw():
    global x
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    background(255,255,255)
    a = 10
    b = 10
    for i in range(20):
        ellipse (x,200,a,b)
        a=a+20
        b=b+20
    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    speed=10    
    x=x+speed
    if x == 400:
        speed = speed -20

    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */

         
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
