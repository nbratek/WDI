def liczba_cyfr(x):
    licznik = 0
    while x >0:
        licznik += 1
        x //= 10
    return licznik

def f(x):
    l = liczba_cyfr(x)
    while x > 0:
        y = x % 10
        if y != l:
            x //= 10
        else:
            return True
    return False

n = int(input())
print(f(n))