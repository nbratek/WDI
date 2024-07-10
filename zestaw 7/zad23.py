from list import * 

def liczba_elementow(p):
    licznik = 0
    fast = p
    slow = p
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    fast = fast.next.next
    slow = slow.next
    licznik += 1
    while fast != slow:
        licznik += 1
        slow = slow.next
        fast = fast.next.next
    return licznik