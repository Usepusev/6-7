import module, check
import runagain
import exception_handler
def main():
    try:
        # Основная функция программы. Ввод значений, вызов функции проверки значений, функции проверки существования треугольника
        # a, b, c(str)- переменные для сторон треугольников
        # res(str) - результат проверки
        # bl(bool) - переменная для проверки
        # otvet(str) - переменная для запуска программы заново
        a = input("Введите первую сторону треугольника: ")
        b = input("Введите вторую сторону треугольника: ")
        c = input("Введите третью сторону треугольника: ")
        bl = False

        a, b, c, bl, res = check.check(a, b, c, bl)
        while bl != True:
            print(res)
            a = input("Введите первую сторону треугольника: ")
            b = input("Введите вторую сторону треугольника: ")
            c = input("Введите третью сторону треугольника: ")
            a, b, c, bl, res = check.check(a, b, c, bl)

        if module.treug(a, b, c) == True: print("Такой треугольник существует!")
        else: print("Такого треугольника не существует!")

        runagain.runagain()
    except MemoryError:
        exception_handler.handle_memory()
    except KeyboardInterrupt:
        exception_handler.handle_keyboard_interrupt()
        
if __name__ == "__main__":
    while True:
            main()
            runagain.runagain()