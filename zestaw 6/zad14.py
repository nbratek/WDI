def hanoi_rec(n, b, e, help):
    if n == 1: 
        print(b, e)
        return
    hanoi_rec(n-1, b, help, e)
    print(b, e)
    hanoi_rec(n - 1, help, e, b)


def hanoi(n):
    hanoi_rec(3, 'A', 'B', 'C')
   