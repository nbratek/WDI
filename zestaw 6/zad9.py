def odwazniki(T, i, p, w = []):
    if p == 0:
        print(w)
        return True
    if p == len(T):
        return False
    return odwazniki(T, i + 1, p, w) or odwazniki(T, i + 1, p - T[i], w +[T[i]]) or odwazniki(T, i + 1, p + T[i], w +[-T[i]])
