from math import sqrt

def prime_number(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i - 1 <= int(n ** 0.5) + 1:
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
        i += 6
    return True


def apply_mask(a, b, n):
    y = 1
    s = 0 
    while a > 0:
        if n % 2 == 0:
            s = s + (a % 10) * y
            a //= 10
        else: 
            s = s + (b % 10) * y 
            b //= 10
        n //= 2
        y *= 10
        
    return s 

def get_number_of_decimal_digits(x):
    count = 0 
    while x > 0:
        x = x // 10
        count += 1
    return count

def digits(a, b, n):
    dl_a = get_number_of_decimal_digits(a)
    dl_b = get_number_of_decimal_digits(b)
    licznik_a = 0
    licznik_b = 0
    while n > 0:
        if n % 2 == 0:
            licznik_a += 1
        else:
            licznik_b += 1 
        n //= 2
    if licznik_a <= dl_a and licznik_b == dl_b:
        return True
    return False

def check(a, b):
    count = 0
    n = 0 
    num_of_digits_a = get_number_of_decimal_digits(a)
    num_of_digits_b = get_number_of_decimal_digits(b)
    max_mask = 2 ** (num_of_digits_a + num_of_digits_b)
    while max_mask - 1 > n: 
        if digits(a, b, n) and prime_number(apply_mask(a, b, n)):
            print(apply_mask(a, b, n))
            count += 1
        n += 1
    return count

a = int(input())
b = int(input())
print(check(a, b))