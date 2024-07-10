def f(x):
    return 1 / x

def pole(k, n):
    s = 0 
    x = (k - 1) / n
    srodek = 1 + (k - 1) / 2 * n
    for i in range(k):
        s += f(srodek)
        srodek += x
    return s * x

n = int(input())
k = int(input())
print(pole(k,n))

