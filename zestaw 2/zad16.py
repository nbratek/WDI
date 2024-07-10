
def czynniki_pierwsze(x):
    suma = 0 
    l = x
    for i in range(2, x):
        if  l % i == 0:
            while l % i == 0:
                suma += suma_cyfr(i)
                l //= i
    return suma

def suma_cyfr(x):
    l = x
    suma_c = 0 
    while l > 0:
        y = l % 10
        suma_c += y
        l //= 10
    return suma_c


for i in range(1000001):
    if czynniki_pierwsze(i) == suma_cyfr(i):
        print(i)