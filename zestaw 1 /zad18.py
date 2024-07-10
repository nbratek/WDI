def pierw_newton(n):
    x = 1
    y = n
    eps = 10 ** (-6)
    while abs(x - y) > eps: 
        x = (x + x + y) / 3
        y = n / (x * x)
    return x
  
n = int(input())
print(pierw_newton(n))