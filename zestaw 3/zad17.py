def prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 6
    while i - 1 <= int(n ** 0.5) + 1:
        if n % (i - 1) == 0:
            return False
        if n % (i + 1) == 0:
            return False
        i += 6
    return True

def get_number_of_decimal_digits(x):
    count = 0 
    while x > 0:
        x = x // 10
        count += 1
    return count

