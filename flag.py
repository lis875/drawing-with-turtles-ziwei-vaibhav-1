from turtle import *

### Functions for drawing
# Modify the code in this function

def bar(bar_color):
    fillcolor(bar_color)
    begin_fill()
    forward(300)
    right(90)
    forward(50)
    right(90)
    forward(300)
    right(90)
    forward(50)
    right(90)
    end_fill()

def star():
    fillcolor("black")
    begin_fill()
    for i in range(5):
        forward(20)
        left(72)
        forward(20)
        right(144)
    end_fill()

    # for j in range(5):
    #     forward(50)
    #     right(144)

### Main code that gets run, to draw the german flag
# Do not modify code below this line for Exercise 7.  It is OK to add code below this for Exercise 8

bar("red")
right(90); forward(50); left(90)
bar("yellow")
right(90); forward(50); left(90)
bar("green")
forward(135)
penup()
left(90)
forward(30)
right(90)
pendown()
star()

done()

    
