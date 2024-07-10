def partition(n, limit, k, T):
    if n == 0:
        wypisz_sume(T, k)
        return
    for i in range(1, limit + 1):
        T[i] = k 
        partition(n - i, min(n - i, i), k + 1, T) 


def full_partition(n):
    T = [0] * n
    partition(n, n - 1, 0, T)

def wypisz_sume(T, k):
    for i in range(0, k - 1):
        print(f"{T[i]} + 1", end ="")
    print(T[k - 1])