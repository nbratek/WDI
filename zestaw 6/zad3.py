def krol(T, w, k, koszt):
    if k == 7:
        return koszt
    m = krol(T, w + 1, k, koszt + T[w + 1][k])
    if k != 0:
        x = krol(T, w + 1, k - 1, koszt + T[w + 1][k - 1])
        if x < m:
            m = x
    if k != 7:
        x = krol(T, w + 1, k + 1, koszt + T[w + 1][k + 1])
        if x < m:
            m = x
    return m 

def main(T, k):
    return krol(T, 0, k, T[0][k])

    