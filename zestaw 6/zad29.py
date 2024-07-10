def subsets(T, A, i, licznik, r):
    if i == len(T) and licznik > 2:
        return check(T, A, r)
    A[i] = 0
    if subsets(T, A, i + 1, licznik, r):
        return True
    A[i] = 1
    if subsets(T, A, i + 1, licznik + 1, r):
        return True
    
def main(T, r):
    return subsets(T, [0]* len(T), 0 , 0, r)

def check(T, A, r):
    x, y, z = 0, 0, 0
    licznik = 0 
    for i in range(len(A)):
        if A[i] == 1:
            x += T[i][0]
            y += T[i][1]
            z += T[i][2]
            licznik += 1
    x = x / licznik
    y = y / licznik
    z = z / licznik 
    if r ** 2 >= x ** 2 + y ** 2 + z ** 2:
        return True
    return False