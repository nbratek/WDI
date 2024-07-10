def dzielenie(N, a):
    T = [0] * (2 * N)
    x = 10
    i = 0 
    while i < 2 * N:
        while x < a:
            x *= 10
            T[i] = 0
            i += 1
        T[i] = x // a
        x = (x % 10) * 10
        i += 1
    return T
