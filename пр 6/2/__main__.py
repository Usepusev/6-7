import module, check
import runagain
import exception_handler
def main():
    # Основная функция программы. Ввод значений, вызов функции проверки значений, функции расчёта
    # points(str)- переменная для списка чисел
    # res(str) - результат проверки
    # bl(bool) - переменная для проверки
    # sredneesrednee(float) - среднее число
    try:
        points = input("Введите числа через пробел: ").split()
        bl = False

        points, bl, res = check.check(points, bl)
        while bl != True:
            print(res)
            points = input("Введите числа через пробел: ").split()
            points, bl, res = check.check(points, bl)
        srednee = module.srednee(points)
        print(f"Среднее чисел равно - {srednee:.2f}")
    except MemoryError:
        exception_handler.handle_memory()
    except KeyboardInterrupt:
        exception_handler.handle_keyboard_interrupt()


if __name__ == "__main__":
    while True:
            main()
            runagain.runagain()