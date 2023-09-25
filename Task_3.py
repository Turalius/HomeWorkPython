def powers_of_two(N):
    power = 0
    result = 1
    
    while result <= N:
        print(result)
        power += 1
        result = 2 ** power

# Например N
N = 100

print("Целые степени двойки, не превосходящие", N, ":")
powers_of_two(N)
