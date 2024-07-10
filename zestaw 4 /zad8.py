from random import randint
def ciag(T, wiersz, kolumna):
    max_licznik = 1
    l = 1
    n = len(T)
    q = T[wiersz + 1][kolumna + 1] / T[wiersz][kolumna]
    while wiersz + 1 < n and kolumna + 1 < n:
        if T[wiersz][kolumna] * q == T[wiersz + 1][kolumna+1]:
            wiersz += 1
            kolumna += 1 
            l += 1
        else: 
            if max_licznik < l:
                max_licznik = l
            l = 1
            q = T[wiersz + 1][kolumna + 1] / T[wiersz][kolumna]
    return l

def f(T):
    n = len(T)
    max_dl = 0
    for i in range(n-1):
        l = ciag(T, i, 0)
        if max_dl < l:
            max_dl = l
    for i in range(n-1):
        l = ciag(T, 0, i)
        if max_dl < l:
            max_dl = l
    return max_dl


T = [
    [1,2,3,4,5],
    [1,1,2,9,34],
    [2,4,9,1,27],
    [3,3,1,27,3],
    [1,1,1,16,1]
    ]
print(f(T))
