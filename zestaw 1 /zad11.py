def zaprzyjaznione(a, b): 
    suma_a = 1
    suma_b = 1
    for i in range(2, a): 
        if a % i == 0: 
            suma_a += i
    for i in range(2, b): 
        if b % i == 0:
            suma_b += i
    if a == suma_b and b == suma_a: 
        return True
    else: 
        return False


n = int(input())
m = int(input())
print(zaprzyjaznione(n, m))