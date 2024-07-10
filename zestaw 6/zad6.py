def suma(T, s_e , s_i, i, flaga):
    if flaga is True and s_e == s_i:
        return s_e
    if i == len(T):
        return float("inf")
    s1 = suma(T, s_e + T[i], s_i + i, i+1, True)
    s2 = suma(T, s_e, s_i, i + 1, flaga)
    return min(s1, s2)

def f(T):
    r = suma(T, 0, 0, 0, False)
    if r == float("inf"):
        return None
    return r

