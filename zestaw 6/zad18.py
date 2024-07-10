def cyfry(a, b):
    x = b
    while x > 9:
        x //= 10
    y = a % 10
    if y < x:
        return True
    return False

def ruch(T, w, k, n_w, n_k):
    n = len(T)
    if n_w >= 0 and n_k >= 0 and n_k < n and n_w < n:
        if cyfry(w, k, n_w, n_k):
            return True
    return False

def krol(T, w, k):
    if w + 1 == 7 and k + 1 == 7:
        return True
    if ruch(T, w, k, w, k + 1):
        if krol(T, w, k + 1):
            return True
    if ruch(T, w, k, w + 1, k):
        if krol(T, w + 1, k):
            return True
    if ruch(T, w, k, w + 1, k + 1):
        if krol(T, w + 1, k + 1):
            return True
    return False
    
    
    
        