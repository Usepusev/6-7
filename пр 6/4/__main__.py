import module, check

while True:
    a = input("Введите первую сторону треугольника: ")
    b = input("Введите вторую сторону треугольника: ")
    c = input("Введите третью сторону треугольника: ")
    bl = False

    a, b, c, bl, res = check.check(a, b, c, bl)
    while bl != True:
        print(res)
        a = input("Введите первую сторону треугольника: ")
        b = input("Введите вторую сторону треугольника: ")
        c = input("Введите третью сторону треугольника: ")
        a, b, c, bl, res = check.check(a, b, c, bl)

    if module.treug(a, b, c) == True: print("Такой треугольник существует!")
    else: print("Такого треугольника не существует!")

    otvet = input('Вы хотите продолжить? Если да, то введите "Y", если нет, то введите "N": ')
    if otvet != 'Y': break