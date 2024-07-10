from math import sqrt

def pierwsze(x):
    if x <= 1: 
        return False
    for i in range(2, int(sqrt(x) )+ 1):
        if x % i == 0:
            return False
    return True


n = int(input())
print(pierwsze(n))