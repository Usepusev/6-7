def mediana(points):
    # Функция расчёта медианы
    points = sorted(points)
    if (len(points) % 2) == 1:
        return points[len(points)//2]
    else:
        return 0.5 * (points[len(points) // 2 - 1] + points[len(points) // 2])
