import turtle
t = turtle.Pen()
turtle.bgcolor("purple")
colors = ["blue", "yellow", "red", "orange"]
number_of_circles = int(turtle.numinput("Количество окружностей", "Сколько окружностей в вашей розетке?", 6))
for x in range(number_of_circles):
    t.pencolor()
    t.circle(100)
    t.left(360/number_of_circles)
