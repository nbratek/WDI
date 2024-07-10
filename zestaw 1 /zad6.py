def f(x):
    y = x ** x - 2020
    return y 

def bisekcja(): 
    eps = 10 *(-6)
    a, b = 0, 100 
    while abs(a - b) > eps:
        x = (a + b) / 2
        if f(x) == 0: 
            return x 
        elif f(x) * f(a) < 0: 
            b = x
        elif f(x) * f(b) < 0: 
            a = x 
    print ((a + b) / 2)


        

