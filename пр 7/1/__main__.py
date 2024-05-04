# main.py
import exception_handler
import word_processor

def main():
    # Основная функция программы. Ввод слов в массив, вызов функции удаления слов и исключений
    # words - список слов для обработки
    # word - переменная для добавления слова в список или пропуска, если слово уже есть
    # response - переменная для запуска программы заново
    try:
        words = []
        while True:
            word = input("Введите слово и нажмите Enter. Пустая строка начнёт работу программы: ")
            if not word:
                break
            words.append(word)
        unique_words = word_processor.get_unique_words(words)
        print("Unique words:")
        for word in unique_words:
            print(word)
    except Exception as e:
        exception_handler.handle_exception(e)
    except KeyboardInterrupt:
        exception_handler.handle_keyboard_interrupt()

if __name__ == "__main__":
    while True:
        main()
        response = input("Вы хотите начать заново? (y/n): ")
        if response.lower() != "y":
            break