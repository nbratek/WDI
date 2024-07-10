from list import create_from_list, print_all
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

def liczba_jedynek(n):
    licznik = 0
    while n > 0:
        if n % 2 == 1:
            licznik += 1
            n //= 2
        else: 
            n //= 2
    if licznik % 2 == 1:
        return True
    return False

def delete(head):
    p = head
    while p is not None:
        if liczba_jedynek(p.val) is True:
            if p.prev is None:
                head = p.next
                if p.next is not None:
                    p.next.prev = None
            else:
                p.prev.next = p.next
                if p.next is not None:
                    p.next.prev = p.prev
        p = p.next
    return head


a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9, 10, 13, 12])
b = delete(a)
print_all(b)