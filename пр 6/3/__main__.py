import module, check
import runagain
import exception_handler

def main():
    # Основная функция программы. Ввод значений, вызов функции проверки, функции расчёта
    # points(str) - переменная для списка чисел
    # res - результат проверки
    # bl(bool) - переменная для проверки
    # mediana(float) - медиана из module
    try:
        points = input("Введите числа через пробел: ").split()
        bl = False

        points, bl, res = check.check(points, bl)
        while bl != True:
            print(res)
            points = input("Введите числа через пробел: ").split()
            points, bl, res = check.check(points, bl)
        mediana = module.mediana(points)
        print(f"Медиана последовательности: {mediana:.2f}")
    except MemoryError:
        exception_handler.handle_memory()
    except KeyboardInterrupt:
        exception_handler.handle_keyboard_interrupt()


if __name__ == "__main__":
    while True:
            main()
            runagain.runagain()