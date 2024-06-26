import exceptions
import morse_code
import runagain
def main():
    # Основная функция программы. Ввод значений, вызов функции перевода на морзянку и исключений
    # user_input(str) - переменная для ввода текста
    # morse_text(str) - результат перевода текста на азбуку морзе
    while True:
        try:
            user_input = input("Введите текст для шифрования в азбуке Морзе: ")
            morse_text = morse_code.text_to_morse(user_input)
            print(f"Шифр в азбуке Морзе: {morse_text}")
            runagain.runagain()
        except MemoryError:
            exceptions.handle_memory()
        except KeyboardInterrupt:
            exceptions.handle_keyboard_interrupt()
        except Exception as e:
            exceptions.handle_exception(e)
if __name__ == "__main__":
    main()