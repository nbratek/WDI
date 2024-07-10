def pole(K):
    return (K[1] - K[0]) * (K[3] - K[2])

def nachodza(K1, K2):
    x1, y1 = K1[0], K1[2]
    x2, y2 = K1[1], K1[3]
    x3, y3 = K2[0], K2[2]
    x4, y4 = K2[1], K2[3]
    if (x1 < x3 < x2 or x1 < x4 < x2) and (y1 < y3 < y4 or y1 < y4< y2):
        return False
    return True

def check(wybrane):
    for i in range(13): 
        for j in range(i + 1, 13):
            if nachodza(wybrane[i], wybrane[j]):
                return False
    s = 0
    for i in range(13):
        s += pole(wybrane[i])
    if s == 2012:
        return True
    return False

def kwadraty(K, wybrane, licznik, i):
    if licznik == 13:
        return check(wybrane)
    wybrane[licznik] = K[i]
    r = kwadraty(K, wybrane, licznik + 1, i + 1)
    if r:
        return True
    return kwadraty(K, wybrane, licznik, i + 1)

def main(K):
    return kwadraty(K, [0] * 13, 0, 0)