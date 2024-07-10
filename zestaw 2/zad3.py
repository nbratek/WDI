def palindrom1(a):
    b = a
    r = 0 
    while b > 0:
        r *= 10
        r += b % 10
        b //= 10
    if r == a: 
        return True
    else: 
        return False
  

a = int(input())
print(palindrom1(a))
    