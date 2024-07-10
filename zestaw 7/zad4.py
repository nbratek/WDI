from list import *

def reverse(head):
    p = None
    while head is not None:
        tmp = head
        head = tmp.next
        tmp.next = p
        p = tmp
    return p

# 1. jesli lista sklada sie z 1 elementu to go zwroc
# 2. W p.p odwroc liste zaczynajaca sie w nastepnym elemencie 
# 3. Na koniec odwroconej listy z kolejnego elementu doczep element aktualny 


def reverse2(p):
    if p.next is None:
        return p
    else:
        prev = reverse2(p.next)
        q = prev
        while q.next is not None:
            q = q.next

        q.next = p
        return prev


a = create_from_list([5, 3, 4, 9, 11, 23, 45])
b = reverse(a)
print_all(b)