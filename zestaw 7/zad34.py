from list import *
def delete(p, k):
    usunieto = False
    t = p.next
    while t != p:
        licznik = 1
        v = t.next
        while v != t:
            if v.val == t.val:
                licznik += 1
            v = v.next
        if licznik == k: #nowa lista z guardem
            usunieto = True
            head = Node(0)
            tail = head
            sent = head
            v = t.next
            while v != t: # dodaj nowe elementy inne niz t.val do nowej listy 
                if v.val != t.val:
                    tail.next = v
                    v = v.next 
                    tail = tail.next 
                else:
                    v = v.next
            head = head.next #zrob cykl z nowej listy
            tail.next = head
            if tail == sent:
                return None, True
            p = head
            t = p 
        t = t.next
    return p, True