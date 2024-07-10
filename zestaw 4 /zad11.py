from random import randint
def przyjaciolki(a):
    cyfry = [False for _ in range(10)]
    while a > 0:
        x = a % 10 
        cyfry[x] = True
        a //= 10 
    return cyfry

def f(T):
    n = len(T)
    licznik = 0
    for i in range(n): 
        for j in range(n):
            if i - 1 >= 0 and przyjaciolki(T[i][j]) != przyjaciolki(T[i - 1][j]):
                continue
            if j - 1 >= 0 and przyjaciolki(T[i][j]) != przyjaciolki(T[i][j - 1]):
                continue
            if i + 1 < n and przyjaciolki(T[i][j]) != przyjaciolki(T[i + 1][j]):
                continue
            if j + 1 < n and przyjaciolki(T[i][j]) != przyjaciolki(T[i][j + 1]):
                continue
            licznik += 1 
    return licznik


T = [[randint(1, 100) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(f(T))