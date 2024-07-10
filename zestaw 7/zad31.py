from list import *

def rozdziel(p):
    even = None
    odd = None
    licznik = 0 
    while p is not None:
        tmp = p.next
        if p.val % 2 == 0 and p.val > 0:
            p.next = even 
            even = p
        elif p.val % 2 == 1 and p.val < 0:
            p.next = odd
            odd = p
        else: 
            p.next = None
            licznik += 1
        p = tmp
    return licznik, even, odd