import random
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]
def random_spyral () :
    t.pencolor(random.choice(colors))
    thick = random.randrange(1, 6)
    sides = random.randrange(3, 8)
    size = random.randint(10, 40)
    x = random.randrange(0, turtle.window_width()//2)
    y = random.randrange(0, turtle.window_height()//2)
    t.penup()
    t.setpos(x, y)
    t.pendown()
    for n in range(size):
        t.forward(n*2)
        t.left(360/sides + 1)

    t.penup()
    t.setpos(-x, y)
    t.pendown()
    t.width(thick)
    for n in range(size):
        t.forward(n*2)
        t.left(360/sides + 1)

    t.penup()
    t.setpos(-x, -y)
    t.pendown()
    t.width(thick)
    for n in range(size):
        t.forward(n*2)
        t.left(360/sides + 1)

    t.penup()
    t.setpos(x, -y)
    t.pendown()
    t.width(thick)
    for n in range(size):
        t.forward(n*2)
        t.left(360/sides + 1)
for m in range(50):
    random_spyral()

