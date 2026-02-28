import turtle
import colorsys
import random

wn = turtle.Screen()
wn.tracer(0) ## with wn.update(), renders the picture instantly

michealangelo = turtle.Turtle()
michealangelo.hideturtle()

def reset(t): ## used to easily re-initialize the turtle for each phase of drawing 
    t.up()
    t.setheading(0)

def drawlogs(t, pos):
    x = pos[0]
    y = pos[1]
    reset(t)
    t.goto(x, y)
    for i in range(2): ## draws each log twice in a different colour to create an outline
        t.pensize(30)
        t.color("saddle brown")
        t.left(20)
        for i in range(2): 
            t.down()
            t.forward(130)
            t.left(180)
            t.color("sienna")
            t.pensize(20)
        reset(t)
        t.goto(x, y + 45)
        t.right(40)


def drawfire(t, pos):
    x = pos[0]
    y = pos[1]
    reset(t)
    t.goto(x, y)
    size = 20
    for i in ["yellow", "orange", "red"]: ## repeats the drawing of the flame 3 times, each time slightly smaller to create layers to the flame
        if i == "red":
            t.begin_fill()
        t.down()
        t.pensize(size)
        t.color(i)
        t.left(70)
        t.circle(130, 40)
        t.right(150)
        t.circle(-130, 30)
        t.setheading(0)
        t.left(70)
        t.circle(130, 50)
        t.right(150)
        t.circle(-150, 60)
        if i == "red":
            t.forward(15)
            t.end_fill()
        size -= 9
        reset(t)
        t.goto(x, y)


def drawgrass(t):
    reset(t)
    y = -340
    t.pensize(15)
    col = ["green", "forest green", "dark green"]
    t.setx(-(turtle.window_width()/2)) 
    t.sety(y)
    t.down()
    while y >= -turtle.window_width()/2: ## changes the turtles colour every 20 pixels, creates a more interesting grass texture!
        for i in range(int(turtle.window_width()/20)):
            t.color(col[random.randint(0, 2)])
            t.forward(20)
        t.up()
        t.setx(-turtle.window_width()/2)
        y -= 15
        t.sety(y)
        t.down()


def drawstar(t, size, pos, col): ## draws a star!
    reset(t)
    x = pos[0]
    y = pos[1]
    random.seed(x)
    t.right(random.randint(0, 360)) ## creates a random offset for each star but uses the stars position as a seed so that the picture is the same every time
    t.pensize(1)
    t.color(col)
    t.goto(x, y)
    t.down()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def drawstarrysky(x): ## uses randomization to populate the sky with stars, eliminating the need to manually input new coordinates for each star 
    newseed = 0
    for i in range(x):  
        random.seed(1000524656 + newseed) ## ensures that the same picture is drawn every time 
        x = random.uniform(-700,700)
        y = random.uniform(0,530)
        drawstar(michealangelo, 12, [x, y], "white")
        newseed += 1


def drawmountains(t): 
    reset(t)
    t.goto(-(turtle.window_width()/2), -220)
    t.color("gray")
    t.pensize(30)
    t.down() 
    for i in range(2):
        t.left(32)
        t.begin_fill()
        t.forward(290)
        t.right(83)
        t.forward(73)
        t.left(93)
        t.forward(349)
        t.right(111)
        t.forward(249)
        t.left(140)
        t.forward(344)
        t.right(133)
        t.forward(440)
        t.left(110)
        t.forward(200)
        t.right(103)
        t.forward(400)
        t.right(30)
        t.forward(2000)
        t.right(90)
        t.forward(2000)
        t.end_fill()
        t.setheading(0)
        t.goto(-(turtle.window_width()/2), -220)
        t.color("darkgray")
        t.pensize(10)


def drawmoon(t, pos):
    reset(t)
    t.goto(pos[0], pos[1])
    t.left(180)
    t.color("light goldenrod yellow")
    t.down()
    t.begin_fill()
    t.circle(75, 180)
    t.left(135)
    t.circle(-106.05, 90)
    t.end_fill()


def drawgradient(t): ## draws the background sky gradient for the picture
    reset(t)
    t.setx(-(turtle.window_width()/2)) 
    t.sety((turtle.window_height()/2))
    h = 271/100
    s = 1
    v = 1
    for i in range(int(turtle.window_height())):
        t.color(colorsys.hsv_to_rgb(h, s, v)) ## converters from the HSV format to RGB, as HSV values allow for a smoother gradient 
        t.forward(int(turtle.window_width()))
        t.up()
        t.forward((-int(turtle.window_width())))
        t.left(-90)
        t.forward(1)
        t.right(-90)
        t.down()
        h = h + .00011



"""
order of drawing is important!! for example, the sky gradient
can not be drawn last as it would overwrite the other elements 
already drawn in the picture
"""

drawgradient(michealangelo)
drawstarrysky(30)
drawstar(michealangelo, 18, [240, 400], "yellow") ## north star!
drawmoon(michealangelo, [50, 460])

drawmountains(michealangelo)
drawgrass(michealangelo)

drawfire(michealangelo, [-420, -380])
drawlogs(michealangelo, [-430, -420])

wn.update()
turtle.exitonclick()