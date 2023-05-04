answer = input("Хотите увидеть спираль? да/нет:")
if answer == 'да':
    print("работаем...")
    import turtle
    t = turtle.Pen()
    t.width(2)
    turtle.bgcolor("black")
    colors = "orange"
    t.pencolor(colors)
    for x in range(200):
        t.forward(x*2)
        t.left(89)
    print("Ну вот, готово!")
