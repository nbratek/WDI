from random import randint
def liczba_jedynek(x):
    l = 0 
    while x > 0:
        a = x % 2
        if a == 1:
            l += 1
        x //= 2
    return l

def f(T1, T2):
    n = len(T1)
    m = len(T2)
    for i in range(m - n + 1): 
        for j in range(m - n + 1):
            licznik = 0
            for x in range(n):
                for y in range(n):
                    if liczba_jedynek(T1[x][y]) == liczba_jedynek(T2[i + x][y + j]):
                        licznik += 1
            if licznik / (n * n) > (1 / 3):
                return True
    return False

T1 = [[randint(0, 20) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T1[i])

T2 = [[randint(0, 20) for _ in range(8)]for _ in range(8)]
for i in range(8):
    print(T2[i])

print(f(T2, T1))