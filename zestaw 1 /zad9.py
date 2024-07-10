def podzielniki(x): 
    for i in range(1, x + 1): 
        if x % i == 0: 
            print(i)

n = int(input())
print(podzielniki(n))