from turtle import *

### Function that draws stars of different sizes
# Do not modify code in this section

def star(size):
    for i in range(5):
        forward(size)
        right(144)

def move_turtle():
    penup()
    forward(100)
    pendown()

### Main code area
# Modify code below this line


star(25)
move_turtle()
star(50)
move_turtle()
star(100)

done()

