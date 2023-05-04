import random
the_number = random.randint(1, 100)
guess = int(input("Угадай число от 1 до 100: "))
attempt = (0)
while guess != the_number:
    attempt + 1
    if guess > the_number:
        delta = guess - the_number
        if delta >= 40:
            print(guess, " - это СЛИШКОМ много. ")
        elif delta > 10 and delta <40:
            print("Моё число меньше твоего")
        else:
            print("Ты близок! Надо только ввести число немного поменьше.")
    if guess < the_number:
        delta = the_number - guess
        if delta >= 40:
            print("число ", guess, " довольно сильно меньше моего.")
        elif delta > 10 and delta < 40:
            print("Моё число больше твоего")
        else:
            print("В этот раз у тебя горяченько.Чуть увеличить, и готово!")
    guess = int(input("Ещё одна попытка... "))
print("Ты угадал! Я загадал число ", guess,"!")
