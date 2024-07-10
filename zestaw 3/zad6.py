from random import randint

def nieparzyste(x):
    while x > 0:
        a = x % 10
        if a % 2 == 1:
            return True
        x //= 10
    return False
        
            
def f(N): 
    T = [0 for _ in range(N)]
    for i in range(N):
        T[i] = randint(1, 1000)
        print(T[i])
    for i in T:
        if nieparzyste(i) is False:
            return False
    return True


n = int(input())
print(f(n))