from list import *
def wielomian(w1, w2):
    p = None 
    while w1 is not None and w2 is not None:
        r = Node(w1.val - w2.val)
        r.next = p
        p = r
        w1 = w1.next
        w2 = w2.next
    if w1 is None:
        r = Node(- w2.val)
        r.next = p
        p = r
        w2 = w2.next
    if w2 is None:
        r = Node(w1.val)
        r.next = p
        p = r
        w1 = w1.next
    return p 