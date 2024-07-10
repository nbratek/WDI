def podciag(T): 
    max_suma_rosnacego = 1
    max_suma_malejacego = 1
    licznik_m = 1
    licznik_r = 1
    new_r = 0 
    for i in range(1, len(T) - 1):
        r = T[i] - T[i - 1]
        if r != new_r:
            new_r = r
            if r > 0:
                licznik_r = 2
                licznik_m = 0 
            else: 
                licznik_m = 2
                licznik_r = 0
                r = T[i] - T[i - 1]
        else:
            if r > 0:
                licznik_r += 1
                if max_suma_rosnacego < licznik_r:
                    max_suma_rosnacego = licznik_r
            else:  
                licznik_m += 1
                if max_suma_malejacego < licznik_m:
                    max_suma_malejacego = licznik_m
        roznica = max_suma_rosnacego - max_suma_malejacego
    return roznica

T = [2, 4, 6, 8, 10, 12, 14, 16, 27, 24, 21, 18, 1, 5, 7]
print(podciag(T))