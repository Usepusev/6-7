import module, check

while True:
    points = input("Введите числа через пробел: ").split()
    bl = False

    points, bl, res = check.check(points, bl)
    while bl != True:
        print(res)
        points = input("Введите числа через пробел: ").split()
        points, bl, res = check.check(points, bl)

    mediana = module.mediana(points)

    print(f"Медиана последовательности: {mediana:.2f}")

    otvet = input('Вы хотите продолжить? Если да, то введите "Y", если нет, то введите "N": ')
    if otvet != 'Y': break