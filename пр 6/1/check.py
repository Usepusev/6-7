def check(katet1, katet2, bl):
    #  Функция проверки введёных переменных на допустимость к расчётам
    try:
        katet1 = float(katet1)
        katet2 = float(katet2)
        bl = True
        res=""
        if katet1 > 0 and katet2 > 0:
            return [katet1, katet2, bl, res]
        elif katet1 <= 0 or katet2 <= 0:
            res="Вы ввели '0' либо отрицательное число"
            katet1 = ""
            katet2 = ""
            bl = False
            return [katet1, katet2, bl, res]
    except ValueError:
        res="Вы ввели не число!"
        katet1 = ""
        katet2 = ""
        bl = False
        return [katet1, katet2, bl, res]