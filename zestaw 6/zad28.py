def jedynki(n):
    licznik = 0 
    while n > 0: 
        if n % 2 == 1:
            licznik += 1
        n //= 2
    return licznik

def f(T, i, s1, s2, s3):
    if i == len(T):
        if s1 == s2 == s3:
            return True
        return False
    if f(T, i + 1, s1 + jedynki(T[i]), s2, s3) or f(T, i + 1, s1, s2 + jedynki(T[i]), s3) or f(T, i + 1, s1, s2, s3 + jedynki(T[i])):
        return True
    return False

def main(T):
    return f(T, 0, 0, 0, 0)