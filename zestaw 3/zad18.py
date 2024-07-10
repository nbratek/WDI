def palindrom(T):
    n = len(T)
    max_dl = 0 
    for i in range(n):
        for j in range(n - 1, -1, -1):
            licznik = 0
            k = 0 
            while i < n and j >= 0 and T[i + k] % 2 == 1 and T[i + k] == T[j - k]:
                licznik += 1
                k += 1
            if max_dl < licznik:
                max_dl = licznik
    return max_dl

T = [12, 2, 3, 7, 5, 9, 5, 7, 3, 2, 4, 1, 11, 15, 11, 1, 4]
print(palindrom(T))
