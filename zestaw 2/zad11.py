def f(a):
    r = a % 10 
    while a > 0:
        a //= 10
        p = a % 10
        if r >= p:
            r = p
        else: 
            return False
    return True

n = int(input())
print(f(n))