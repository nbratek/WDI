def fib(n): 
    a, b = 1, 1
    while b < n: 
        a, b = b, a + b
    return b


n = int(input())
print(fib(n))