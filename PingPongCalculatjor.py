def convert_in2cm(inches):
    return inches * 2.54
def convert_ib2kg(pounds):
    return pounds / 2.2
height_in = int(input("Введите свой рост в дюймах: "))
weight_ib = int(input("Введите мсвой вес в футах: "))
height_cm = convert_in2cm(height_in)
weight_kg = convert_ib2kg(weight_ib)
ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)
feet = height_in // 12
inch = height_in % 12
print("при росте", feet, "футов,", inch, "дюймах и весе", weight_ib, "фунтов, ваш рост", ping_pong_tall, "шариков для пинг понга, а вес сопоставим с", ping_pong_heavy, "шариками для пинг понга")
