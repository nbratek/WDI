from list import *

def delete(p, n):
    s1 = Node()
    s1.next = p
    p = s1
    s2 = Node()
    s2.next = n
    n = s2
    licznik = 0 
    t = n
    while t.next is not None:
        v = p
        flag = False
        while v.next is not None and v.next.val <= t.next.val:
            if v.next.val == t.next.val:
                flag = True
                v.next = v.next.next
                t.next = t.next.next
                licznik += 2
            else: 
                v = v.next
        if not flag:
            t = t.next
    return licznik
