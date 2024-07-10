def is_prime(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    d = 5
    while int(x**0.5) + 1 > d:
        if x % d == 0:
            return False
        d += 2
        if x % d == 0:
            return False
        d += 4
    return True

def pociecie(T, p = 0):
    if p == len(T):
        return True
    n = 0 
    for i in range(p, min(len(T), 30)):
        n = n * 2 + T[i]
        if is_prime(n) and pociecie(T, i + 1):
            return True
        return False                  