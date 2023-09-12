import turtle
from math import radians, cos

def square(length: int)-> None:
    """ draws a square of length 'length' """
    for side in range(4):
        turtle.forward(length)
        turtle.right(90)




def encirled_square(length: int)->  None:
    #draws square n then encloses it inside a circle 
    square(length)
    angle= radians(45)
    radius= length * cos(angle)
    turtle.right(135)
    turtle.circle(radius)
    turtle.right(135)
    print(f'inside function, namespace is: {dir()}')
    print(f'locals{locals()}')


encirled_square(300)
"""
turtle.speed('fast')
for s in range(72):
    #square(120) #passing length 
    encirled_square(120)
    turtle.left(5)
turtle.done() #if u dont put done then the drawing wil disappear 
"""

















