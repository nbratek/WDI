def odwazniki(T, i = 0, p=9):
    n = len(T)
    if p == 0:
        return True
    if p < 0 or i > n - 1:
        return False
    return odwazniki(T, i + 1, p) or odwazniki(T, i + 1, p - T[i])
