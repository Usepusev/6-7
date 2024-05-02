def handle_value():
    print("Ошибка введённого значения!")

def handle_exception(e):
    print(f"Возникла ошибка: {e}")

def handle_keyboard_interrupt():
    print("Возникла ошибка клавиатуры. Работа программы остановлена.")

__all__ = ['handle_value', 'handle_exception', 'handle_keyboard_interrupt']