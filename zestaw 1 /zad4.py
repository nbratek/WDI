n = int(input())
suma = 0 
licznik = 0
i = 1 
while suma < n: 
    licznik += 1
    suma += (2*i - 1)
    i += 1
if suma == n: 
    print(licznik)
else: 
    print(None)
