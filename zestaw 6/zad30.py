def subsets(T, A, i, licznik, r, k):
    if i ==len(T) and licznik % 3 == 0 and licznik > k:
        return check(T, A, r)
    A[i] = 0
    if subsets(T, A, i + 1, licznik, r, k):
        return True
    A[i] = 1
    if subsets(T, A, i + 1, licznik + 1, r, k):
        return True
    
def main(T, r, k):
    return subsets(T, [0] * len(T), 0, 0 , r, k)

def check(T, A, r):
    x, y = 0, 0
    licznik = 0 
    for i in range(len(A)):
        if A[i] == 1: 
            x += T[i][0]
            y += T[i][1]
    x = x / licznik
    y = y / licznik
    if r ** 2 < x ** 2 + y ** 2:
        return True
    return False 