from math import sqrt

def czynniki(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % (i * i) == 0:
            return False
    return True

def iloczyn(T):
    max_dl = 1
    il = 1
    licznik = 1 
    n = len(T)
    for i in range(n):
        if czynniki(T[i]): 
            il *= T[i]
            for j in range(i + 1, n - 1):
                if czynniki(il):
                    il *= T[j]
                    licznik += 1
            if max_dl < licznik:
                max_dl = licznik
    return licznik


T = [2,23,33,35,7,4,6,7,5,11,13,22]
print(iloczyn(T))