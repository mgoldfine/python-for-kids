import random #Запуск библиотеки "random" (рандом)
import json #Запуск библиотеки json, позволяющей подключать к программе файл с данными (например списком городов)
#Функция  определяет последнюю букву города
def town_last_letter(town):
    if town[-1] != "ь" and town[-1] != "ы":
        last_letter_town = town[-1].upper()
    else:
        last_letter_town = town[-2].upper()
        #если последняя буква города Ь или Ы то учитывать предпоследнюю
    return last_letter_town
#Проверка пользователя
def town_check (town):
    if town.upper().replace("Ё", "Е").replace("-", " ") in another_list:
        return ("город " + town + " уже был")
        #Контроль повторений пользователя
    elif town.upper().replace("Ё", "Е").replace("-", " ") not in upper_towns and town != "выйти":
        return ("Нет такого города")
        #В случае ошибки или неправильного города программа об этом говорит
    elif town[0].upper() != first_letter and town != "выйти" and first_letter != "":
        return ("Твой город начинается не на ту букву")
        #Сообщение о том на ту ли букву ввёл пользователь город
    else:
        return False
#Определение города компьютера
def computer_town():
    global another_list
    small_list = []#Создание пустого списка
    for town2 in towns:
        if town2.upper()[0] == last_letter_town.upper() and town2 not in another_list:
            small_list.append(town2)
            #добавляем в пустой список все города начинающися на нужную букву
    my_town = random.choice(small_list)#Рандомно выбрать из списка город
    another_list.append(my_town.upper().replace("Ё", "Е").replace("-", " "))#Проверять был ли уже такой город
    if town != "выйти":#проверять не ввёл ли пользователь выйти
        return (my_town)#Напечатать свой город
    else:
        return ("Поиграем как нибудь ещё!")

with open('towns.json', mode="r", encoding="utf-8") as f:#Присоеденение файла с городами 
    towns: object = json.load(f) #Записываем список городов в переменную towns (города)
upper_towns = []
for upper_town in towns:
    upper_towns.append(upper_town.upper().replace("Ё", "Е").replace("-", " "))
another_list = []#Создаём пустой список под названием Another_list (другой список) чтобы записывать туда использованные города, и не повторяться
town = "" #Создаём переменную town (город) значение которой будет меняться каждый раз когда пользователь вводит название города
first_letter = "" #В переменную first_letter (первая буква) записываем что в начале игры, поскольку ещё никто не называл городов там может быть любая буква
print("Правила игры:\nдумаю правила игры в города знают все, поэтому напоминать нет смысла. Я должен отметить лишь одно: пиши название города ПРАВИЛЬНО")
while town != "выйти": #Выполнять цикл, пока пользователь не выйдет
    if first_letter == "":#Если  это первый раз, и нет никакой заданной буквы то
        town = input("Введи город на любую букву или 'выйти', чтобы закончить игру\n")# показывать на экране фразу: "Введи город на любую букву или "выйти", чтобы закончить игру"
    else: #Если наоборот то
        input_text = "Тебе на букву " + first_letter + "\n"#Говорить пользователю на какую букву должен быть его город
        town = input(input_text)
    check = town_check(town)
    if check != False:
        print(check)
        continue
    another_list.append(town.upper().replace("Ё","Е").replace("-", " "))
    last_letter_town = town_last_letter(town)
    my_town = computer_town()
    print(my_town)
    first_letter = town_last_letter(my_town)
