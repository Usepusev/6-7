# word_processor.py
def get_unique_words(words):
    """
    Возвращает список уникальных слов.
    Args:Список слов
    Returns:unique_words Список уникальных слов
    """
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return unique_words