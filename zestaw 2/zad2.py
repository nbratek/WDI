def f(a, b, n):
    print(a//b, "." if a % b != 0 else "", sep="", end="")
    r = a % b
    for i in range(n): 
        r = 10 * r 
        print(r // b, end="")
        r = r % b
        



a = int(input())
b = int(input())
n = int(input())
print(f(a, b, n))