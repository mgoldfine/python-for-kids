import turtle
t = turtle.Pen()
number = int(turtle.numinput("Количество сторон или окружностей", "Сколько сторон или окружностей будет у фигуры?", 6))
shape = turtle.textinput("Какую фигуру вы хотите?", "Введите 'м' для многоугольника, 'к' для круга, или 'в', чтобы выйти")
for x in range (number):
    if shape == 'к':
        t.circle(100)
    elif shape == 'м':
        t.forward(150)
    t.left(360/number)
