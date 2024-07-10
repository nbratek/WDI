from math import sqrt
def pierwsze(x):
    if x < 2: 
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

#1

def wykresl(x, A):
    n = 0 
    j = 0 
    for i in range(len(A)):
        y = x % 10
        if A[i] == 0:
            n = y * (10 ** j) + n
            j += 1
        x //= 10
    return n 



def main(x):
    n = 0 
    y = x
    while y > 0:
        n += 1
        y //= 10
    all_subsets(x, n)

def all_subsets(x, n):
    A = [0 for i in range(n)]
    return subsets(x, A, 0, n)

def subsets(x, A, k, n):
    if k == n:
        return check(x, A)
    if A[k] == 0:
        subsets(x, A, k + 1, n)
    if A[k] == 1:
        subsets(x, A, k + 1, n)
    
def check(x, A):
    j = 0 
    for i in range(len(A)):
        if A[i] == 1:
            j += 1
        if j >= 1:
            n = wykresl(x, A)
            if n >= 10 and pierwsze(n):
                print(n)

#2
def wykreslanie(x, n = 0, j = 0, a = False):
    if x == 0:
        if n > 9 and a and pierwsze(n):
            print(n)

    else:
        wykreslanie (x // 10, ((10 ** j) * (x % 10)) + n, j + 1, a)
        wykreslanie (x // 10, n, j, True)