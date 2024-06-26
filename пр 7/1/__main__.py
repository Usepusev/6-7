# main.py
import exception_handler
import word_processor
import runagain
def main():
    # Основная функция программы. Ввод слов в массив, вызов функции удаления слов и исключений
    # words(list) - список слов для обработки
    # unique_words - список уникальных слов
    # word(str) - переменная для добавления слова в список или пропуска, если слово уже есть
    try:
        words = []
        while True:
            word = input("Введите слово и нажмите Enter. Пустая строка начнёт работу программы: ")
            if not word:
                break
            words.append(word)
        unique_words = word_processor.get_unique_words(words)
        print("Уникальные слова:")
        for word in unique_words:
            print(word)
    except MemoryError:
        exception_handler.handle_memory()  
    except Exception as e:
        exception_handler.handle_exception(e)
    except KeyboardInterrupt:
        exception_handler.handle_keyboard_interrupt()

if __name__ == "__main__":
    while True:
            main()
            runagain.runagain()