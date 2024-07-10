from list import *

def liczba(n):
    l_jedynek = 0
    l_dwojek = 0
    while n > 0:
        if n % 3 == 1:
            l_jedynek += 1
            n //= 3
        if n % 3 == 2:
            l_dwojek += 1
            n //= 3
        if n % 3 == 0:
            n //= 3
    if l_jedynek > l_dwojek:
        return True
    return False

def delete(head):
    p = head
    while p.next is not None:
        if liczba(p.next.val) is True:
            p.next = p.next.next
        else:
            p = p.next 
    return head

a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9, 10, 13, 12])
b = delete(a)
print_all(b)