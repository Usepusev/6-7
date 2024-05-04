import exceptions
import coin_combinations

def main():
    # Основная функция программы. Ввод значений, подсчёт, вызов функции расчёта
    # target_sum - сумма для расчёта монетами
    # target_sum_cents - сумма для расчёта монетами в центах
    # num_coins - количество монет для расчёта суммы
    # coins - массив возможных монет
    # combinations - массив с комбинацией монет для размена
    # response - переменная для запуска программы заново
    while True:
        try:
            target_sum = float(input("Введите сумму: $"))
            num_coins = int(input("Введите количество монет: "))
            
            coins = [1, 5, 10, 25]
            target_sum_cents = int(target_sum * 100)
            combinations = coin_combinations.get_coin_combinations(coins, target_sum_cents, num_coins, current_combination=None)

            if combinations:
                print(f"Да, можно набрать ${target_sum:.2f} с помощью {num_coins} монет.")
                print("Возможные комбинации:")
                for combination in combinations:
                    print(combination)
            else:
                print(f"Нет, невозможно набрать ${target_sum:.2f} с помощью {num_coins} монет.")
            response = input("Хотите начать с начала? (y/n): ")
            if response.lower() != "y":
                break
        except ValueError:
            exceptions.handle_value()
        except KeyboardInterrupt:
            exceptions.handle_keyboard_interrupt()
        except Exception as e:
            exceptions.handle_exception(e)
if __name__ == "__main__":
    main()