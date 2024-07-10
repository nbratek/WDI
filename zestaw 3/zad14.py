from random import randint

def prawdopodobienstwo(N, m): 
    licznik = 0
    for i in range(m):
        year = [0 for _ in range(366)]
        for j in range(N):
            birthday = randint(0, 364)
            year[birthday] += 1
        for k in range(365):
            if year[k] > 1:
                licznik += 1
                break
    return licznik / m


N = int(input())
m = int(input())
print(prawdopodobienstwo(N, m))