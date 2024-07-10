def odwazniki(T, i = 0, p = 0, l = 0):
    if p == l:
        return True
    if i > len(T) - 1:
        return False
    return odwazniki(T, i + 1, p + T[i], l) or odwazniki(T, i + 1, p, l + T[i]) or odwazniki(T, i + 1, p, l)
