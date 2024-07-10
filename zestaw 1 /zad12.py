def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
m = int(input())
o = int(input())
solution = nwd(nwd(n, m), o)
print(solution)