def f(n):
    a0 = 0 
    a1 = 1
    b0 = 2
    while n != a0:
        print(b0)
        a = a1 - (b0 * a0)
        b = b0 + 2 * a0
        a0 = a1
        a1 = a
        b0 = b

n = int(input())
print(f(n))