def treug(a, b, c):
    # Функция подсчёта площади треугольника
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s
