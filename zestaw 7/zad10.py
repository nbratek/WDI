from list import *

def reverse(head):
    p = None
    q = head.next
    while head is not None:
        head.next = p 
        p = head
        head = q
        if q.next is not None:
            q = q.next
    return p

def push_back(l, val):
    if l is None:
        return Node(val)
    while l.next is not None:
        l = l.next
    l.next = Node(val)


def dodaj(p, q):
    if p is None:
        return q 
    if q is None:
        return p
    r1 = reverse(p)
    r2 = reverse(q)
    s = 0
    n = None
    while r1 is not None or r2 is not None:
        suma = s
        if r1 is not None:
            suma += r1.val
            r1 = r1.next
        if r2 is not None:
            suma += r2.val
            r2 = r2.next
        s = suma / 10
        a = suma % 10
        push_back(n, a)
    if s != 0:
        push_back(n, s)
    t = reverse(n)
    return t
