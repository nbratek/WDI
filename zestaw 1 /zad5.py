def pierw_newton(n):
    x = 1
    y = n
    eps = 10 ** (-6)
    while abs(x - y) > eps: 
        x = (x + y) / 2
        y = n / x
    print(x) 
  
n = int(input())
print(pierw_newton(n))