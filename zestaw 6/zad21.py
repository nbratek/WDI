def check(T, s, n_s, i, j, wiersze, kolumny):
    if n_s == s:
        return True
    if n_s > s:
        return False
    if j >= len(T):
        i += 1
        j = 0
    if i >= len(T):
        return False
    if wiersze[i] is False and kolumny[j] is False:
        wiersze[i] = True
        kolumny[j] = True
        if check(T, s, n_s + T[i][j], i, j + 1, wiersze, kolumny):
            return True
        wiersze[i] = kolumny[j] = False
    if check(T, s, n_s, i, j + 1, wiersze, kolumny):
        return True
    return False

def suma(T):
    n = len(T)
    wiersze = [False] * n 
    kolumny = [False] * n
    s = int(input())
    return check(T, s, 0, 0, 0, wiersze, kolumny)


#2 
def rek(T, s, n_s, i, kol):
    n = len(T)
    if i == n and n_s == s:
        return True
    for j in range(n): #kolumny
        if kol[j] is False:
            if rek(T, s, n_s, i + 1, kol):
                return True
            kol[j] = True
            if rek(T, s, n_s +T[i][j], i + 1, kol):
                return True
            kol[j] = False
    return False
    

def main(T, s):
    n = len(T)
    kol = [False] * n
    return rek(T, s, 0, 0, kol)
