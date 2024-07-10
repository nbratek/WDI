from math import sqrt 

def f(a, b): 
    eps = 10 * (-6)
    while abs(a - b) > eps: 
        a, b = sqrt(a * b), (a + b) / 2
    return a

n = int(input())
m = int(input())
print(f(n, m))