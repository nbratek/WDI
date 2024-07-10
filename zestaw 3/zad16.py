from math import inf

def check(T): 
    n = len(T)
    licznik_najmniejszej = 0
    licznik_najwiekszej = 0 
    najmniejsza = inf
    najwieksza = - inf
    for i in range(n): 
        if T[i] < najmniejsza:
            najmniejsza = T[i]
        if T[i] > najwieksza:
            najwieksza = T[i]
    for i in range(n):
        if T[i] == najmniejsza:
            licznik_najmniejszej += 1
        if T[i] == najwieksza:
            licznik_najwiekszej += 1
    if licznik_najmniejszej == 1 and licznik_najwiekszej == 1: 
        return True
    else: 
        return False
    
T = [5, 7, 12, -9, 10, -17, 1, 13]
print(check(T))