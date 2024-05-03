import module, check

while True:
    # Основная функция программы. Ввод значений, вызов функции проверки значений, функции расчёта
    points = input("Введите числа через пробел: ").split()
    bl = False

    points, bl, res = check.check(points, bl)
    while bl != True:
        print(res)
        points = input("Введите числа через пробел: ").split()
        points, bl, res = check.check(points, bl)

    srednee = module.srednee(points)

    print(f"Среднее чисел равно - {srednee:.2f}")

    otvet = input('Вы хотите продолжить? Если да, то введите "Y", если нет, то введите "N": ')
    if otvet != 'Y': break