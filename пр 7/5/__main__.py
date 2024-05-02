import exceptions
import coin_combinations

def main():
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