import random
choises = ["камень","ножницы","бумага"]
print("Камень давит ножницы, ножницы режут бумагу, а бумага накрывает камень.Замкнутый круг да?")
player = input("Выбери одно из трёх, или нажми пробел, чтобы закончить игру")
while player != " ":#Играть пока пользователь не выйдет
    player = player.lower()#Поменять ввод пользователя на нижний регистр
    computer = random.choice(choises)#Выбрать один из предметов
    print("Перед тем как ты назвал "+player+" я выбрал "+computer+".")
    if player == computer:
        print("У нас ничья!")
    elif player == "камень":
        if computer == "ножницы":
            print("Поздравляю, ты меня одолел!")
        else:
            print("Я победил!")

    elif player == "бумага":
        if computer == "камень":
            print("Вот ты и победил!")
        else:
            print("Поздравляю с проигрышем!")
    elif player == "ножницы":
        if computer == "бумага":
            print("Победа за тобой!")
        else:
            print("Не всегда видишь ли везёт тебе!")
    else:
        print("Так нечестно..!")
    print()#Пропустить строку
    player = input("Выбери одно из трёх, или нажми пробел, чтобы закончить игру")



