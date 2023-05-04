driving_age = eval(input("Каков минимальный вазраст для получения прав в вашей стране? "))
your_age = eval(input("Сколько вам лет? "))
if your_age >= driving_age:
    print("Вы достаточно взрослый для получения прав")
if your_age < driving_age:
    if driving_age - your_age > 4:
        print("Извините вы не можете водить, ещё", driving_age - your_age, "лет")
    if driving_age - your_age == 1:
        print("Извините вы не можете водить, ещё ", driving_age - your_age, "лет")
    if driving_age - your_age!= 1 and driving_age - your_age <= 4:
        print("Извините вы не можете водить, ещё ", driving_age - your_age, "года")

