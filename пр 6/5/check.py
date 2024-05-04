def check(a, b, c, bl):
    # Функция проверки введённых значений на допустимость к расчётам
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a+b>c and a+c>b and b+c>a:
            bl = True
            return [a, b, c, bl]
        else:
            print("Такого треугольника не существует!")
            a = ""
            b = ""
            c = ""
            bl = False
            return [a, b, c, bl]
    except ValueError:
        print("Вы ввели что-то не то!")
        a = ""
        b = ""
        c = ""
        bl = False
        return [a, b, c, bl]