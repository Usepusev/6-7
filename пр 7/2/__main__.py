from exceptions import *
import count_range
import runagain

def main():
    while True:
    # Основная функция программы. Ввод значений, вызов функции подсчёта чисел и исключений
    # list_input(str) - переменная для ввода строки чисел разделенных запятыми list_input
    # list_numbers(list) - переменная с массивом чисел полученным из введёного 
    # min_bound(int) и max_bound(int) - целочисленные переменные границ
    # result(int) - количество чисел в границах
        try:
            list_input = input("Введите список чисел (разделённый запятыми): ")
            list_numbers = [int(x) for x in list_input.split(",")]
            min_bound = int(input("Введите минимальную границу: "))
            max_bound = int(input("Введите максимальную границу: "))
            result = count_range.count_range(list_numbers, min_bound, max_bound)
            print(f"Количество элементов [{min_bound}, {max_bound}]: {result}")
        except ValueError:
            handle_value()
        except Exception as e:
            handle_exception(e)
        except KeyboardInterrupt:
            handle_keyboard_interrupt()
        runagain.runagain()

if __name__ == "__main__":
    main()