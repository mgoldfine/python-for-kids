import datetime
red = input("Как тебя зовут?\n")
time = datetime.datetime.now()
x = time.hour
if x >= 4 and x < 12:
    print("Доброе утро, "+ red+ "!")
if x >= 12 and x < 18:
    print("Добрый день, "+ red+ "!")
if x >= 18 and x < 22:
    print("Добрый вечер, "+ red+ "!")
if x >= 22 or x < 4:
    print("Спокойной ночи, "+ red+ "!")



