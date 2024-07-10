from random import randint
def nieparzyste(x):
    while x > 0:
        if x % 2 == 0:
            return False
        x //= 10 
    return True

def f(T):
    for row in T:
        for n in row:
            if nieparzyste(n) is True:
                break
        else:
            return False
    return True


def np_w_wierszu(tab):
    for n in tab: 
        if nieparzyste(n):
            return True
    return False

def f2(T):
    for i in range(len(T)):
        if not np_w_wierszu(T[i]):
            return False
    return True        

T = [[randint(1, 100) for _ in range(4)]for _ in range(4)]
for i in range(4):
    for j in range(4):
        print(T[i][j], end=' ')
print(f(T))