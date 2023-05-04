# SquareSpiral2.py - Рисование квадратной спирали
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
f = input("На какой угол поворачивать?\n")
sides = eval(input("Введите количество сторон от 2 до 7: "))
d = ["red", "orange", "yellow", "green", "#4682B4", "blue", "purple"]
for x in range(200):
    t.pencolor(d[x%sides])
    t.circle(x * 3/sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/200)
    print(x)
print("картинка нарисована")

