def count_range(numbers, min_bound, max_bound):
    """
    Подсчитывает количество элементов в списке, имеющим границы заданные пользователем
    Args:
        numbers (список): Список чисел.
        min_bound (int): Минимальная граница.
        max_bound (int): Максимальная граница.
    Returns:
        Целое число: Количество элементов.
    Raises:
        InvalidInputError: Если ввод остался пустым или значения чисел введены неправильно.
    """
    if not numbers:
        raise InvalidInputError("Ввод пуст")
    if min_bound > max_bound:
        raise InvalidInputError("Неправильное значение")
    return sum(1 for num in numbers if min_bound <= num <= max_bound)