def f(a, b, podstawa):
    A = [False for _ in range(podstawa)]
    B = [False for _ in range(podstawa)]

    while a > 0:
        c = a % podstawa
        A[c] = True
        a //= podstawa
    
    while b > 0:
        c = b % podstawa
        B[c] = True
        b //= podstawa
    
    for i in range(len(A)):
        if A[i] is True and B[i] is True:
            return False
    return True

def check(a, b):
    for i in range(2, 17):
        if f(a, b, i) is True:
            return i
    return False

a = int(input())
b = int(input())
print(check(a, b))
