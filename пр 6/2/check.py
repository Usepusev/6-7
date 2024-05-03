def check(points, bl):
    # Фугкцтя проверки введённых значений на допустимость расчётов
    try:
        for i in range(len(points)):
            points[i] = float(points[i])
        bl = True
        res = ""
        return points, bl, res
    except ValueError:
        res ="Вы ввели что-то не то!"
        points = []
        bl = False
        return points, bl, res