def czynniki(x):
    A = []
    for i in range(2, x):
        if x % i == 0:
            A.append(i)
            while x % i == 0:
                x //= i
    return A

def skok(T, i, licznik):
    if i == len(T) - 1:
        return licznik
    if i == len(T):
        return False
    k = czynniki(T[i])
    for j in range(len(k)):
        if k[j] + i < len(T) and k[j] < T[k[j] + i]:
            skok(T, i + k[j], licznik + 1)

    

def main(T):
    return skok(T, 0, 0)
