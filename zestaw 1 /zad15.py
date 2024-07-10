from math import sqrt

x = sqrt(0.5)
y = sqrt(0.5 + 0.5 * x)
wynik = 1
n = int(input())
for i in range(n): 
    wynik *= x
    x = y

pi = 2 / wynik
print(wynik)

