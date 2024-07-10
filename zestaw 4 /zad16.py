from random import randint
def pierwsze(x):
    while x > 0:
        a = x % 10
        if a != 2 or a != 3 or a != 5 or a != 7:
            return False
        x //= 10
    return True

def liczba(tab): 
    for n in tab:
        if pierwsze(n) is True:
            return True
    return False

def f(T): 
    for i in range(len(T)):
        if liczba(T[i]) is False:
            return False
    return True

T = [[randint(0, 10) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(f(T))
