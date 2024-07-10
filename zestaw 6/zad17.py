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

def n_of_digits(n): 
    if n == 0:
        return 0
    return 1 + n_of_digits(n//10)

def numbers_to_digits_array(n):
    d = n_of_digits
    T = [0] * d
    numbers_tda(T, n, d - 1)
    return T

def numbers_tda(T, n, k):
    if n == 0:
        return 
    last = k % 10
    T[k] = last
    numbers_tda(T, n // 10, k - 1)

def main(x, y):
    T1 = numbers_to_digits_array(x)
    T2 = numbers_to_digits_array(y)
    return liczba(T1, T2, 0, 0, 0)

def liczba(T1, T2, k1, k2, suma):
    if k1 == len(T1):
        while k2 < len(T2):
            suma = suma * 10 + T2[k2]
            k2 += 1
        if is_prime(suma):
            return 1
        return 0
    if k2 == len(T2):
        while k1 < len(T1):
            suma = suma * 10 + T1[k1]
            k1 += 1
        if is_prime(suma):
            return 1
        return 0
    wynik = 0
    wynik += liczba(T1, T2, k1 + 1, k2, suma * 10 + T1[k1])
    wynik += liczba(T1, T2, k1, k2 + 1, suma * 10 + T2[k2])
    return wynik