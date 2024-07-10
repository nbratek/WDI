def f(n):
    a = 2
    while a <= n: 
        if n % a == 0: 
            return True
        a = 3 * a + 1
    return False


n = int(input())
print(f(n))