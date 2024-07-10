def dlugosc(n, p):
    dl = 0
    while n > 0:
        dl += 1
        n //= p
    return dl


def zamiana(n, p):
    znaki = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
    l = dlugosc(n, p)
    T = [0 for _ in range(l)]
    i = 0
    while n > 0:
        T[i] = znaki[n % p]
        n //= p
        i += 1
    for j in range(len(T) - 1, -1, -1): 
        print(T[j])


n = int(input())
for p in range(2, 17):
    print(p)
    print(zamiana(n, p))