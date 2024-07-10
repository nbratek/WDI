#1
def wyznacznik(A, n, skreslone, kolumna):
    if kolumna == n - 1:
        w = 0 
        for i in range(n):
            if skreslone[i] == False:
                w = i 
        return A[w][n - 1]
    suma = 0
    for i in range(n):
        if skreslone[i] == False:
            skreslone[i] = True
            suma += (-1) **(i + kolumna) * A[i][kolumna] * wyznacznik(A, n, skreslone, kolumna + 1)
            skreslone[i] = False
    return suma

def main(A, n):
    skreslone = [False] * n
    return wyznacznik(A, n, skreslone, 0)

#2
def tab(b_T, i):
    s_t = [[0 for _ in range(len(b_T) - 1)]for _ in range(len(b_T) - 1)]
    i = 0 
    for j in range(len(b_T)):
        for k in range(len(s_t)):
            s_t[i][k] = b_T[j][k + 1]
        i += 1
    return s_t


def f(T):
    if len(T) == 2:
        return T[0][0] * T[1][1] - T[0][1] * T[1][0]
    det = 0 
    for i in range(len(T)):
        det += (-1) **(i) * T[i][0] * f(tab(T, i))

    return det