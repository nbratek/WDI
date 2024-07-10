def fib(n):
    a, b = 1, 1
    while a <= n:
        if n % a == 0:
            x = a
            y = b
            while y <= n:
                if y * a == n:
                    return True
                x, y = y, x + y
        
        a, b = b, a + b
    return False

n = int(input())
print(fib(n))