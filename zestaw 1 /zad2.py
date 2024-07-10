year = 2023
min_suma = year + 1 
best = (0, 2023)
for i in range(1, 2024):
    a = i 
    b = 2023
    while a > 0 and a < b: 
        a, b = b - a, a
    if a + b < min_suma:
        min_suma = a + b 
        best = (a, b)
print (min_suma, best)