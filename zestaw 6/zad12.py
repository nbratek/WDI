def iloczyn(T, i, n, p, w=[]):
    if n == 0 and p == 1:
        for i in range(len(w)):
            print(w[i])
        return 1
    if n == 0: 
        return 0
    licznik = 0 
    for i in range(len(T)):
        if p % T[i] == 0:
            w += [T[i]]
            licznik += iloczyn(T, i+ 1, n - 1, p / T[i], w)
    return licznik