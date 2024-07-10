def f(liczba):
    while liczba > 1:
        if liczba % 2 == 0:
            liczba //= 2
        elif liczba % 3 == 0:
            liczba //= 3
        elif liczba % 5 == 0:
            liczba //= 5
        else:
            return False
    if liczba == 1:
        return True
    else: 
        return False
        
def dtp(n):
    licznik = 1 
    for i in range(1, n + 1):
        if f(i) == True: 
            licznik += 1
    return licznik

n = 20
print(dtp(n))