from random import randint

def podciag(N):
    T = [randint(100, 1000) for _ in range(N)]
    for i in range(N):
        print(T[i])
    max_suma = 0
    for i in range(N):
        for j in range(N - 1, -1):
            licznik = 0
            k = 0 
            while i + k < N and j - k >= 0 and T[i + k] == T[j - k]:
                licznik += 1
                k += 1
            if max_suma < licznik:
                max_suma = licznik
    return max_suma


N = int(input())
print(podciag(N))