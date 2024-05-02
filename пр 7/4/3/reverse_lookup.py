def reverse_lookup(dictionary, value_to_search):
    """
    Находит все ключи в словаре по введённому значению
    Args:
        dictionary (dict): Словарь для поиска значений в нём.
        value_to_search (any): Значения для поиска.

    Returns:
        list: Список ключей с введённым значением.
    """
    if not isinstance(dictionary, dict):
        return 1  # Error code: invalid dictionary
    if value_to_search is None:
        return 2  # Error code: invalid value to search
    return [key for key, value in dictionary.items() if value == value_to_search]