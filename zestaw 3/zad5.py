T = []
licznik = 0
while True:
    n = int(input())
    if n != 0: 
        T.append(n)
        licznik += 1
    else:
        break

for i in range(licznik):
    for j in range(licznik - i - 1):
        if T[j] < T[j + 1]:
            T[j], T[j + 1] = T[j + 1], T[j]
print(T[9]) 
            

