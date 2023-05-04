# SpiralMyName.py - печатает цветную спираль из имени пользователя
import turtle # установка графики Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red","yellow","blue","green","orange","white","purple"]
# Запрос имени пользователяс помощью всплывающего окна textinput
e = eval(input("Сколько вы хотите сторон у спирали?\n"))
your_name = turtle.textinput("Введите своё имя","Как тебя зовут?")
# Нарисовать на экране спираль из имени, повторённого 100 раз
for x in range(100):
    t.pencolor(colors[x%e]) # По очереди выбрать все 4 цвета
    t.penup() # Не рисовать обычные линии спирали
    t.forward(x*e) # Просто переместить черепашку по экрану
    t.pendown() # Написать имя пользователя, увеличивая каждый раз шрифт
    t.write(your_name,font = ("Arial",int((x + e) /  e),"bold"))
    t.left(360+1) # Повернуть налево как в других спиралях
