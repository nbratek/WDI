from math import sqrt, inf
def srodek_ciezkosci(C):
    n = len(C)
    if n == 0: 
        return inf, inf
    x, y = 0, 0
    for i in range(n):
        x += C[i][0]
        y += C[i][1]
    x /= n
    y /= n
    return x, y

def odleglosc(A, B):
    if A == (inf, inf) or B == (inf, inf):
        return inf
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)

def f(T, i = 0, A = [], B = []):
    if i == len(T):
        return odleglosc(srodek_ciezkosci(A),srodek_ciezkosci(B))
    return min(f(T, i + 1, A + [T[i]], B) or f(T, i + 1, A, B + [T[i]]) or f(T, i + 1, A, B))
