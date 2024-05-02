def get_coin_combinations(coins, target_sum_cents, num_coins, current_combination=None):
    """
    Выводит все возможные комбинации монет для введённой суммы.

    Args:
        coins (list): Список возможных номиналов монет.
        target_sum (int): Сумма для подбора.
        num_coins (int): Количество используемых монет.
    """
    if current_combination is None:
        current_combination = []
    if num_coins == 0:
        if sum(current_combination) == target_sum_cents:
            return [current_combination]
        else:
            return []
    else:
        combinations = []
        for coin in coins:
            new_combination = list(current_combination)  # Create a copy of the current combination
            new_combination.append(coin)  # Add the new coin to the copy
            combinations.extend(get_coin_combinations(coins, target_sum_cents, num_coins - 1, new_combination))
        return combinations