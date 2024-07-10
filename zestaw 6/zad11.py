def iloczyn(T, i, n, p):
    if n == 0:
        return False
    if n == 0 and p == 1:
        return True
    licznik = 0 
    for i in range(len(T)):
        if p % T[i] == 0:
            iloczyn(T, i + 1, n - 1, p / T[i])
            licznik += 1
    return licznik
