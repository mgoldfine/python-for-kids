import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
    def spyral(x, y):
        t.pencolor(random.choice(colors))
        size = random.randint(10, 40)
        t.penup()
        t.setpos(x, y)
        t.pendown()
        for m in range (size):
            t.forward(m*2)
            t.right(200)
turtle.onscreenclick(spyral)
