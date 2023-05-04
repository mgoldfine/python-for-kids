import random
print("Правила игры:\n"
      "В карточной игре Пьяница игроки мешают карты, и чья карта больше, тот и выиграл.\n"
      "После каждой партии вводите [Enter], чтобы вытянуть карту\n")
suits = ["пики", "бубны", "черви", "крести"]
faces = ["двойка", "тройка", "четвёрка", "пятёрка", "шестёрка", "семёрка", "восьмёрка", "девятка", "десятка", "валет", "дама", "король", "туз"]
yes_no = input("Вы хотите играть этот раунд? да/нет ")
my_round_victories = ["Победа в этом раунде победа достаётся мне!", "Не хочу тебя огорчать, но я выиграл"]
your_round_victories = ["Похоже мои шестерёнки надо смазать на удачу", "В этом раунде победа достаётся тебе!"]
while yes_no != "нет":
    my_victories = 0
    your_victories = 0
    draw = 0
    my_victories_list = ["Я победил!", "В этой партии я победил!", "Поздравляю с проигрышем!", "Удача на моей стороне"]
    your_victories_list = ["Ты победил", "Оглянуться не успел, а ты меня уже одолел!", "Даже я не идеален"]
    for x in range(26):
        сonsignment = input("Чтобы вытянуть карту, нажмите [Enter]")
        if сonsignment == "":
            my_face = random.choice(faces)
            my_suit = random.choice(suits)
            your_face = random.choice(faces)
            your_suit = random.choice(suits)
            print("партия №", x + 1 )
            print("У меня", my_face, my_suit, ", а у тебя", your_face, your_suit)
            if faces.index(my_face) > faces.index(your_face):
                my_victory = random.choice(my_victories_list)
                print(my_victory)
                my_victories += 1
            elif faces.index(my_face) < faces.index(your_face):
                your_victory = random.choice(your_victories_list)
                print(your_victory)
                your_victories += 1
            else:
                print("у нас ничья!")
                draw += 1
    print("очки:\nмоих выигрышей: ", my_victories, "\nтвоих выигрышей:", your_victories, "\nничей:", draw )
    if my_victories > your_victories:
        if my_victories - your_victories < 10:
            my_round_victory = random.choice(my_round_victories)
            print(my_round_victory)
        else:
            print("Да ты титан!")
    elif my_victories < your_victories:
        if your_victories - my_victories < 10 :
            your_round_victory = random.choice(your_round_victories)
            print(your_round_victory)
        else:
            print("А я здорово оторвался от тебя!")
    else:
        print("В этом раунде у нас ничья!")
    yes_no = input("Вы хотите играть следующий раунд? да/нет ")




