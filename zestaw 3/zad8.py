def check(T):
    n = len(T)
    A = [False for _ in range(n)]
    A[0] = True
    for i in range(n):
        if A[i] == True:
            temp = T[i]
            k = 2
            while temp != 1:
                while temp % k == 0:
                    if i + k < n:
                        A[i + k]  = True
                    temp = temp / k
                k += 1
    if A[n - 1] == True:
        return True
    return A[n - 1]

T = [6, 1, 5, 2, 4, 3, 9, 9, 1, 2, 4]
print(check(T))