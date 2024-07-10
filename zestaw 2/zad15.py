def f(n): 
    for i in range(10 **(n - 1), 10 ** n):
        l = i 
        suma = 0 
        while l > 0: 
            r = l % 10
            suma += (r ** n)
            l //= 10
        if i == suma:
            print(i)



n = int(input())
print(f(n))
        
