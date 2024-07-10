from math import sqrt

def doskonale(x): 
    suma = 1 
    for i in range (2, x):
        if x % i == 0: 
            suma += i
    if suma == x:
        return True
    else: 
        return False
    
n = int(input())
print(doskonale(n))