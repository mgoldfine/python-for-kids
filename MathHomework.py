print("Math homework")
problem = input("Введите пример или 'q', чтобы выйти: ")
while (problem != "q"):
    print("Ответ на ", problem, "- это", eval(problem))
    problem = input("Введите ещё один пример или 'q', чтобы выйти: ")
