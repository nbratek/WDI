def tablice(T1, T2):
    n = len(T1)
    m = len(T2)
    T3 = []
    i, j = 0,0 
    while i < n and j < m:
        if T1[i] < T2[j]:
            T3.append(T1[i])
            i += 1
        else: 
            T3.append(T2[j])
            j += 1
    while i < n:
        T3.append(T1[i])
        i += 1
    while j < m:
        T3.append(T2[j])
    return T3

def merge(T):
    t = T[0]
    n = len(T)
    for i in range(1, n):
        T = merge(t, T[i])
    return T

def f(T):
    T2 = []
    n = len(T)
    T = merge(T)
    i = 0 
    flag = True
    while i < n - 1:
        if T[i + 1] == T[i]:
            flag = False
            while i < n - 1 and T[i + 1] == T[i]:
                i += 1
        elif T[i+ 1] != T[i]:
            if flag:
                T2.append(T[i])
            flag = True
            i += 1
    if T[n - 1] != T[n - 2]:
        T2.append(T[n - 1])
    return T2
