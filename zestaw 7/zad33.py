from list import *

def slowo(p, val):
    t = p.next
    Napis = False
    while t != p:
        if ord(val[-1]) < ord(t.next.val[0]) and ord(val[0]) > ord(t.val[-1]):
            q = Node(val)
            q.next = t.next
            t.next = q
            Napis = True
        t = t.next
    return Napis