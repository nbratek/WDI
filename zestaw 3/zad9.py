from random import randint

def ciag(N):
    max_suma = 1
    T = [randint(1, 100) for _ in range(N)]
    for i in range(N):
        print(T[i])
    licznik = 1
    for i in range(1, N):
        if T[i - 1] < T[i]:
            licznik += 1
        else:
            if max_suma < licznik:
                max_suma = licznik
                licznik = 1
    return max_suma

n = int(input())
print(ciag(n))