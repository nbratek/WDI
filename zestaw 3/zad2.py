def liczby(a, b):
    T1 = [0 for _ in range(10)]
    T2 = [0 for _ in range(10)]
    while a > 0:
        x = a % 10 
        T1[x] += 1
        a //= 10
    while b > 0:
        y = b % 10 
        T2[y] += 1
        b //= 10
    for i in range(10):
        if T1[i] != T2[i]:
            return False
    return True

n = int(input())
m = int(input())
print(liczby(n, m))

    

