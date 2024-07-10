def fib(x): 
    a, b = 1, 1
    for i in range(x): 
        q = a / b
        print(q)
        a, b = b, a + b


n = int(input())
print(fib(n))