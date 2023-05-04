driving_age = eval(input("Каков минимальный вазраст для получения прав в вашей стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
    print("Вы достаточно взрослый для получения прав")
else:
     print("Извините вы не можете водить, ещё", driving_age - your_age, "лет")

