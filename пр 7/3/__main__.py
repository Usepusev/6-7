import exceptions
import reverse_lookup
import runagain
def main():
    # Основная функция программы. Создание словаря, ввод значения, вызов функции поиска и исключений
    # dictionary(list, const) - словарь с исходными значениями
    # value_to_search(str) - строковая переменная для поиска
    # result - ключи имеющие введённый ключ
    while True:
        try:
            dictionary = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 1, "f":""}
            value_to_search = input("Введите значение для поиска: ")

            result = reverse_lookup.reverse_lookup(dictionary, value_to_search)
            if isinstance(result, int):
                print(f"Ошибка: {result}")
            elif not result:  # Check if result is an empty list
                print(f"Не найдено ключей с значением {value_to_search}")
            else:
                print(f"Ключи с значением {value_to_search}: {result}")

            runagain.runagain()
        except MemoryError:
            exceptions.handle_memory()
        except KeyboardInterrupt:
            exceptions.handle_keyboard_interrupt()
        except Exception as e:
            exceptions.handle_exception(e)
if __name__ == "__main__":
    main()