def podzielniki(n):
    T = [-1] * 20
    i = 0
    k = 2
    while n > 1: 
        if n % k == 0:
            T[i] = k
            i += 1
            while n % k == 0:
                n //= k
        k += 1
    return f(T)

s = 0

def f(T, i = 0 , iloczyn = 1):
    if T[i] == -1: 
        if iloczyn == 1:
            return 0
        global s 
        s += iloczyn
        return
    f(T, i + 1, iloczyn)
    f(T, i + 1, iloczyn * T[i])