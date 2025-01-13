#Nicolas A.
#9/9

#init
import turtle
n= turtle.Turtle()
n.color("purple")
#Functions
def pentagon():
    for i in range(5):
     n.forward(100)
     n.left(72)

#main
n.begin_fill()
pentagon()
n.end_fill()
