import module, check
import runagain
import exception_handler

def main():
    try:
        # Основная функция программы. Ввод значений, вызов функции проверки значений, функции подсчёта площади треугольника
        # a, b, c(str) - переменные для сторон треугольников
        # bl(bool) - переменная для проверки
        # square(float) - площадь треугольника
        a = float(input("Введите первую сторону треугольника: "))
        b = float(input("Введите вторую сторону треугольника: "))
        c = float(input("Введите третью сторону треугольника: "))
        bl = False
        a, b, c, bl = check.check(a, b, c, bl)
        while bl != True:
            a = float(input("Введите первую сторону треугольника: "))
            b = float(input("Введите вторую сторону треугольника: "))
            c = float(input("Введите третью сторону треугольника: "))
            a, b, c, bl= check.check(a, b, c, bl)

        square = module.treug(a, b, c)
        print(f"Площадь треугольника: {square:.2f}")
    except MemoryError:
        exception_handler.handle_memory()
    except KeyboardInterrupt:
        exception_handler.handle_keyboard_interrupt()
if __name__ == "__main__":
    while True:
            main()
            runagain.runagain()
