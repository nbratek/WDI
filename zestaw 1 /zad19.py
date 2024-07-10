def silnia(x):
    s = 1
    for i in range(2, x + 1):
        s *= i
    return s

def f(n):
    e0 = 2
    e = 0
    for i in range(2, n):
        e += 1 / silnia(i) 
    e = e + e0
    return e

n = int(input())
print(f(n))