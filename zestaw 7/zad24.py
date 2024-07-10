from list import *


def liczba_elementow(p):
    fast = p
    slow = p
    while True:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    licznik = 0
    fast = p
    while fast != slow:
        fast = fast.next
        slow = slow.next
        licznik += 1
    return licznik
