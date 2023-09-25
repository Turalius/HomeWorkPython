def heads_or_tails(coins):
    heads = 0
    tails = 0
        
    for coin in coins:
        if coin == 'H':
            heads += 1
        else:
            tails += 1
    
    return min(heads, tails)

# Пример:
coins = ['H', 'T', 'H', 'H', 'T']
min_flips = heads_or_tails(coins)
print("Минимальное количество монет, которые нужно перевернуть:", min_flips)
