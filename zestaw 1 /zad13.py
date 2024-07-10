def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b): 
    x = a * b // nwd(a, b)
    return x

n = int(input())
m = int(input())
o = int(input())

sol = nww(nww(n, m), o)
print(sol)