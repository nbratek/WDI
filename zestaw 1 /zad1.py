
a = 0
b = 1
print(a)
while b < 1000000:
    a, b = b, a + b
    print(a)