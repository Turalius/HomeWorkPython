def find_numbers(S, P):
    for X in range(1, 1001):  
        for Y in range(1, 1001):  
            if X + Y == S and X * Y == P:
                return X, Y  
    return None

# Например:
S = 15
P = 56

result = find_numbers(S, P)

if result:
    X, Y = result
    print(f"Найдены числа X = {X} и Y = {Y}")
else:
    print("Нет подходящих чисел")