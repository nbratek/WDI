from math import sqrt

def iloczyn(n):
    a = int(sqrt(n)) 
    for i in range(a, n):
        if n % i == 0:
            print(a, n // a)
            break

n = int(input())
print(iloczyn(n))