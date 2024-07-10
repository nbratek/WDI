from math import log

def f(x):
    return x ** x - 2020

def pochodna(x):
    return x ** x + (x ** x) * (log(x))

def styczne(a, b):
    eps = 10 ** (-4)
    while abs(a - b) > eps:
        b = a
        a = a - f(a) / pochodna(a)
    return a 

n = int(input())
m = int(input())
print(f(n, m))