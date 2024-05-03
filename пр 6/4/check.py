def check(a, b, c, bl):
    # Функция проверки введённых значений на допустимость расчётов
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        bl = True
        res = ''
        return [a, b, c, bl, res]
    except ValueError:
        res="Вы ввели что-то не то!"
        a = ""
        b = ""
        c = ""
        bl = False
        return [a, b, c, bl, res]