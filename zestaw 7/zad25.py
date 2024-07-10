from list import * 
from zad24 import liczba_elementow

def wskaznik(p):
    l = liczba_elementow(p)
    l = l - 1
    if l < 0: 
        return None
    tmp = p
    while l > 0: 
        l = l - 1
        tmp = tmp.next
    return tmp