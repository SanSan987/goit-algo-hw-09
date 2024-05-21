import timeit

# Реалізація жадібного алгоритму
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    
    return result


# Реалізація алгоритму динамічного програмуваняя
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin
    
    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

amount = 113
amount_big = 100000

# Виконання двох алгоритмів для суми з ДЗ (113)
greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)
print("Жадібний алгоритм:", greedy_result)
print("Алгоритм динамічного програмування:", dp_result)

# Виконання двох алгоритмів з функцією вимірювання часу виконання та для виликих сум
greedy_time = timeit.timeit(lambda: find_coins_greedy(amount_big), number=10)
dp_time = timeit.timeit(lambda: find_min_coins(amount_big), number=10)
print(f"Жадібний алгоритм виконується за {greedy_time / 10:.6f} секунд")
print(f"Алгоритм динамічного програмування виконується за {dp_time / 10:.6f} секунд")