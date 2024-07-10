from random import randint
def parzyste(x):
    while x > 0:
        a = x % 10 
        if a % 2 == 0: 
            return True
        x //= 10
    return False

def wiersz(tab):
    for n in tab:
        if parzyste(n) is False:
            return False
    return True

def f(T):
    for i in range(len(T)):
        if wiersz(T[i]) is True: 
            return True
    return False

T = [[randint(1, 100) for _ in range(4)]for _ in range(4)]
for i in range(4):
    for j in range(4):
        print(T[i][j], end=' ')
print(f(T))