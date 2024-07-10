def czynniki(x):
    if x < 2:
        return 0 
    i = 2
    licznik = 0 
    while x > 1 and i <= x // 2:
        if x % i == 0:
            licznik += 1
            while x % i == 0:
                x //= i
        i += 1
    return licznik

def dl(W):
    n = 0
    for i in range(len(W)):
        n += 1
    generuj_rozbicie(W, n)

def generuj_rozbicie(W, n):
    A = [0] * n
    return rozbicie_rek(A, n, 0, W)    

def rozbicie_rek(A, n, k, W):
    if k == n:
        return same_rozbicie(A, W)
    if A[k] == 0:
        rozbicie_rek(A, n, k + 1, W)
    if A[k] == 1:
        rozbicie_rek(A, n, k + 1, W)
    if A[k] == 2:
        rozbicie_rek(A, n, k + 1, W)
    
def same_rozbicie(A, W):
    for i in range(len(A)):
        if A[i] == 0:
            flaga = False
            for j in range(len(A)):
                if A[j] == 1 and W[i] == W[j]:
                    for k in range(len(A)):
                        if A[k] == 2 and W[i] == W[k]:
                            flaga = True
            if not flaga:
                return False
    return True

def main(T):
    n = len(T)
    W = [0] * n
    for i in range(n):
        W[i] = czynniki(T[i])
    return generuj_rozbicie(W, len(W))        