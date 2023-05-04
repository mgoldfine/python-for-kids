import turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "brown", "gray", "pink"]
famili = []
name = turtle.textinput("Моя семья", "Введите имя или нажмите 's' чтобы выйти:")
while name!= "s":
    famili.append(name)
    name = turtle.textinput("Моя семья", "Введите имя или нажмите 's' чтобы выйти:")
for x in range(100):
    t.pencolor(colors[x%len(famili)])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(famili[x%len(famili)], font = ("Arial",int((x+4)/4), "bold"))
    t.left(360/len(famili) + 2)
