def fib(x):
    a = 1
    b = 1 
    while a * b <= x:
        if a * b == x: 
            return True
        a, b = b, a + b
   
    return False



n = int(input())
print(fib(n))
    