import module, check
import runagain

while True:
    # Основная функция программы. Ввод значений, вызов функции проверки, функции расчёта
    # points(str) - переменная для списка чисел
    # res - результат проверки
    # bl(bool) - переменная для проверки
    # mediana(float) - медиана из module
    points = input("Введите числа через пробел: ").split()
    bl = False

    points, bl, res = check.check(points, bl)
    while bl != True:
        print(res)
        points = input("Введите числа через пробел: ").split()
        points, bl, res = check.check(points, bl)

    mediana = module.mediana(points)

    print(f"Медиана последовательности: {mediana:.2f}")

    runagain.runagain()
