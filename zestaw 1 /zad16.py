def ciag():
    licznik = 0
    wyraz = 0
    for i in range(2, 10001): 
        licznik_i = 0
        a = i
        while a != 1:
            licznik_i += 1
            an = ( a % 2) * (3 * a + 1) + (1 - a % 2) * a / 2
            a = an
        if licznik < licznik_i: 
            licznik = licznik_i
            wyraz = i
    print(wyraz)
    

