import random
# Игровой цикл
keep_going = True
while keep_going:
    # Выброс пяти случайных кубиков
    dice = [0, 0, 0, 0, 0] # Создание массива для 5 значений dice[0]-dice[4]
    for i in range(5): # Бросить случайное число от 1 до 6 для всех пяти костей
        dice[i] = random.randint (1,6)
    print("Вам выпало", dice)
    dice.sort()
    if dice[0] == dice[4]:
        print ("Яцзы!")
    elif dice[0] == dice[3] or dice[1] == dice[4]:
        print("Четыре одинаковых")
    elif dice[0] == dice[2] or dice[1] == dice[3] or dice[2] == dice[4]:
        print("три одинаковых")
    keep_going = (input("Нажми [Enter] для продолжения или любую клавишу чтобы выйти: ") == "")



