import module, check
import runagain
while True:
    # Основная функция программы. Ввод значений, вызов функции проверки значений, функции подсчёта гипотенузы
    # katet1 и katet2(str) - переменные ввода катетов
    # res(str) - результат проверки
    # bl(bool) - переменная для проверки
    # gip(gloat) - гипотенуза из module
    katet1 = input('Введите первый катет: ')
    katet2 = input('Введите второй катет: ')
    bl = False
    
    katet1, katet2, bl, res = check.check(katet1, katet2, bl)
    while bl != True:
        print(res)
        katet1 = input('Введите первый катет: ')
        katet2 = input('Введите второй катет: ')
        katet1, katet2, bl, res = check.check(katet1, katet2, bl)

    gip = module.gip(katet1, katet2)

    print(f"Гипотенуза равна - {gip:.2f}")
    
    runagain.runagain()