from random import randint
#1
def f(T):
    n = len(T)
    for i in range(n):
        w = 0 
        k = 0
        for j in range(n):
            if T[i][j] == 0:
                w = 1
            if T[j][i] == 0:
                k = 1
            if w == 1 and k == 1:
                break
        else:
            return False
    return True    

#2
def f2(T):
    n = len(T)
    w = [False for _ in range(n)]
    k = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if T[i][j] == 0:
                w[i] = True
                k[j] = True
    for i in range(n):
        if w[i] == False:
            return False
    for i in range(n):
        if k[i] == False:
            return False
    return True


T = [[randint(- 2, 2) for _ in range(4)]for _ in range(4)]
for i in range(4):
    print(T[i])

print(f2(T))