#Liam Beck
#9/24
#pd.5

#init
import turtle
import random
turtle.colormode(255)
rng=random
liam=turtle.Turtle()
liam.speed(10)
marco=liam
n=liam
sadie=liam
rngcolor=(rng.randint(0,255),rng.randint(0,255),rng.randint(0,255))
rngposition=(rng.randint(-400,400),rng.randint(-400,400))
#funtions
#draws a starfish at any size, color, and location(last 2 must be in parenthesis)
def patrick(size,angle,color,position):
    liam.left(180)
    liam.penup()
    liam.goto(position)
    liam.pendown()
    liam.color(color)
    liam.left(angle)
    liam.begin_fill()
    liam.width(size/5)
    for i in range(5):
        liam.fd(size)
        liam.left(144)
    liam.end_fill()
    liam.penup()
    liam.left(72)

def draw_seaweed(size,color,x,y):
    marco.penup()
    marco.goto(x,y)
    marco.pendown()
    marco.color(color)
    for i in range(3):
        marco.circle(size,30)
        marco.circle(-size,30)

def fish(size,color,x,y):
    n.penup()
    n.goto(x,y)
    n.pendown()
    n.color(color)
    n.width(size/10)
    n.begin_fill()
    n.left(30)
    n.forward(size)
    n.right(120)
    n.forward(size)
    n.right(120)
    n.forward(size)
    n.end_fill()
    n.dot(size,color)
    n.right(150)

def bubbles(size,color):
    for i in range(1):
        sadie.dot(size,color)
        sadie.penup()
        sadie.goto(random.randint(-400,400), random.randint(-400,400))
        sadie.pendown
#puts all the elements together and has an ocean bg
def ocean():
    liam.dot(1500,18,3,153)
    liam.left(72)
    for i in range(12):
        bubbles(rng.randint(25,100),(rng.randint(0,10),rng.randint(0,25),rng.randint(150,255)))
    for i in range(3):
        patrick(rng.randint(50,150),rng.randint(0,360),(rng.randint(0,255),rng.randint(0,255),rng.randint(0,150)),(rng.randint(-400,400),rng.randint(-450,300)))
    liam.seth(0)
    for i in range(4):
        fish(rng.randint(50,100),(rng.randint(0,255),rng.randint(0,255),rng.randint(0,255)),rng.randint(-400,400),rng.randint(-400,400))
    liam.seth(75)
    for i in range(5):
        liam.width(rng.randint(5,20))
        draw_seaweed(rng.randint(100,250),(rng.randint(0,100),rng.randint(0,255),rng.randint(0,255)),rng.randint(-400,400),rng.randint(-550,-450))

#main
ocean()


    
