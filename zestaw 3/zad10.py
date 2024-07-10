
def ciag(T):
    max_suma = 1
    licznik = 2
    n = len(T)
    r = T[1] - T[0]
    for i in range(1, n):
        if T[i - 1] + r == T[i]:
            licznik += 1
        else:
            if max_suma < licznik:
                max_suma = licznik
                licznik = 2 
                r = T[i] - T[i - 1]
    return max_suma

T = [4, 3, 2, 4, 6, 8, 10, 11, 12, 32]
print(ciag(T))