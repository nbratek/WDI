from random import randint

def podciag(T):
    n = len(T)
    max_dl = 0
    suma_el = 0 
    suma_idx = 0
    licznik = 0
    for i in range(n - 1):
        if T[i] < T[i + 1]:
            suma_el += T[i]
            suma_idx += i 
            licznik += 1
    if suma_idx == suma_el:
        if max_dl < licznik:
            max_dl = licznik 
            return max_dl, suma_el
    else:
        return 0

N = int(input())
T = [randint(0, 50) for _ in range(N)]
for i in range(N):
    print(T[i])
print(podciag(T))