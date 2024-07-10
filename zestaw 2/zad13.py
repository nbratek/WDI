def f(x):
    y = x % 10
    x //= 10
    while x > 0:
        r = x % 10
        if r == y:
            return False
        else: 
            x //= 10
    return True

n = int(input())
print(f(n))