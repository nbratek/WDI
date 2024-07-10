def rez(T, R, i = 0, chosen =[]):
    if len(chosen) == 3:
        return check(chosen, R)
    if i == len(T):
        return False
    return rez(T, R, i + 1, chosen + [T[i]]) or rez (T, R, i + 1, chosen)

def check(chosen, R):
    r1, r2, r3 = chosen
    if r1 + r2 + r3 == R:
        return True
    if 1/R == 1/r1 + 1/r2 + 1/r3:
        return True
    if ((r1 * r2) / (r1 + r2)) + r3 == R or ((r1 * r3) / (r1 + r3)) + r2 == R or ((r3 * r2) / (r3 + r2)) + r1 == R:
        return True
    return False
