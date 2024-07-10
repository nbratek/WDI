def ciag(T):
    max_suma = 1
    licznik = 2
    n = len(T)
    q = T[1] / T[0]
    for i in range(2, n):
        if T[i - 1] * q == T[i]:
            licznik += 1
        else:
            if max_suma < licznik:
                max_suma = licznik
                licznik = 2
                q = T[i] / T[i - 1]
    return max_suma


T = [2, 4, 8, 16, 32, 3, 9, 27, 1, 5, 2, 4, 7, 8]
print(ciag(T))