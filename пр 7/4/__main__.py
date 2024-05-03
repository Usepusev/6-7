import exceptions
import morse_code

def main():
    # Основная функция программы. Ввод значений, вызов функции перевода на морзянку и исключений
    while True:
        try:
            user_input = input("Введите текст для шифрования в азбуке Морзе: ")
            morse_text = morse_code.text_to_morse(user_input)
            print(f"Шифр в азбуке Морзе: {morse_text}")
            response = input("Хотите начать с начала? (y/n): ")
            if response.lower() != "y":
                break
        except KeyboardInterrupt:
            exceptions.handle_keyboard_interrupt()
        except Exception as e:
            exceptions.handle_exception(e)
if __name__ == "__main__":
    main()