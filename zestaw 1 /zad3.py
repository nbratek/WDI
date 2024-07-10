n = int(input())
a = 0
b = 1 
fib_s = 0 
while fib_s < n:
    fib_s += b
    a, b = b, a + b
a = 0
b = 1
while fib_s > n: 
    fib_s -= b
    a, b = b, a + b
if fib_s == n: 
    print ("TAK")
else: 
    print("NIE")