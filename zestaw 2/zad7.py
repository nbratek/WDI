def f(n): 
    for i in range(n): 
        a = i * i + i + 1
        if n % a == 0:
            return True
    else: 
        return False


n = int(input())
print(f(n))