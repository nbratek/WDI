def suma(T, k, i, s1, e1, e2, s2):
    if s1 == s2 and e1 + e2 == k:
        return True
    if i == len(T):
        return False
    return suma(T, k, i + 1, s1, e1, e2, s2) or suma(T, k, i + 1, s1 + T[i], e1 + 1, e2, s2) or suma(T, k, i + 1, s1, e1, e2 + 1, s2 + T[i])



def main(T, k):
    return suma(T, k, 0, 0, 0, 0, 0)