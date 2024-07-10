from math import *

def silnia(x): 
    s = 1
    for i in range(2, x + 1):
        s *= i
    return s

def cos(x):
    n = 5 
    wynik = 0
    for i in range(n):
        wynik += (((-1) ** n) * (x ** (2*i))) / silnia(2 * i)
    return wynik 

x = pi / 2
print(cos(x))