def handle_value():
    # Функция сдерживает ошибку значения и выводит на экран причину
    print("Ошибка введённого значения!")

def handle_exception(e):
    # Функция сдерживает общие ошибки и выводит на экран причину
    print(f"Возникла ошибка: {e}")

def handle_keyboard_interrupt():
    # Функция сдерживает ошибку клавиатуры(Ctrl+c) и выводит на экран причину
    print("Возникла ошибка клавиатуры. Работа программы остановлена.")

__all__ = ['handle_value', 'handle_exception', 'handle_keyboard_interrupt']