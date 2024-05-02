def check(a, b, c, bl):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a+b>c and a+c>b and b+c>a:
            bl = True
            res = ""
            return [a, b, c, bl]
        else:
            res = "Такого треугольника не существует!"
            a = ""
            b = ""
            c = ""
            bl = False
            return [a, b, c, bl, res]
    except ValueError:
        res = "Вы ввели что-то не то!"
        a = ""
        b = ""
        c = ""
        bl = False
        return [a, b, c, bl, res]