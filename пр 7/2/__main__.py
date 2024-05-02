from exceptions import *
import count_range

def main():
    while True:
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
        response = input("Вы хотите начать заново? (y/n): ")
        if response.lower() != "y":
            break

if __name__ == "__main__":
    main()