from math import sqrt
def prime(a):
    i = 2
    if a == 2 or a == 3: return True
    elif a <= 1 or a%2 == 0 or a%3 == 0: return False
    while i <= sqrt(a):
        if a % i == 0: return False
        i += 1
    return True

def dec(n): 
    d = 0
    i = 0
    while n > 0: 
        a = n % 10
        d += a * (2 ** i)
        n //= 10
        i += 1
    return d

def rek(A, B, n):
    if A == 0 and B == 0:
        if not prime(dec(n)):
            return 1
        return 0
    elif A == 0:
        return rek(A, B - 1, n * 10)
    elif B == 0:
        return rek(A - 1, B, n * 10 + 1)
    else: 
        return rek(A, B - 1, n * 10) + rek(A - 1, B, n * 10 + 1)
    
def f(A, B):
    if A == 0:
        return 0
    return rek(A - 1, B, 1)