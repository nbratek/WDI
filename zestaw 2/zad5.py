def apply_mask(x, n):
    y = 1
    s = 0 
    while x > 0:
        if n % 2 == 0:
            s = s + (x % 10) * y
            y *= 10
        n //= 2
        x //= 10
    return s 

def get_number_of_decimal_digits(x):
    count = 0 
    while x > 0:
        x = x // 10
        count += 1
    return count

def check(x):
    count = 0
    n = 0 
    num_of_digits = get_number_of_decimal_digits(x)
    max_mask = 2 ** num_of_digits
    while max_mask - 1 > n: 
        if apply_mask(x, n) % 7 == 0:
            count += 1
        n += 1
    return count

x = int(input())
print(check(x))