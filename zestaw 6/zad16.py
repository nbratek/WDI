samogloski = 'a', 'o', 'y', 'e', 'i', 'u'
def wyraz_helper(s1, s2, T, i):
    if i == len(s2):
        return check(s1, s2, T)
    T[i] = 0
    if wyraz_helper(s1, s2, T, i + 1):
        return True
    T[i] = 1 
    if wyraz_helper(s1, s2, T, i + 1):
        return True
    return False

def wyraz(s1, s2):
    return wyraz_helper(s1, s2, [0] * len(s2), 0)

def waga(s):
    licznik = 0 
    asc = 0 
    for i in s:
        print(i)
        asc += ord(i)
        if i in samogloski:
            licznik += 1
    return licznik, asc

def check(s1, s2, T):
    n = len(s2)
    licznik = 0 
    for i in range(n):
        if T[i] == 1:
            licznik += 1
    A = [0] * licznik
    j = 0 
    for i in range(n):
        if T[i] == 1:
            A[j] = T[i]
            j += 1
    if waga(s1) == samogloski(A):
        return True
    return False   

