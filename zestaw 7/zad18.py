from list import *

def unikalne(head):
    p = head
    while p is not None: 
        q = p
        while q.next is not None:
            if q.next.val == p.val:
                q.next = q.next.next
            else:
                q = q.next
        p = p.next
    return head

def unikalne2(head):
    p = head
    while p is not None:
        q = p.next
        prev = p
        while q is not None:
            if q.val == p.val:
                prev.next = q.next
                q = q.next
            else:
                prev = prev.next
                q = q.next
        p = p.next

    return head

a = create_from_list([3, 6, 1, 4, 1, 7, 2, 5, 3, 9, 10, 13, 12])
b = unikalne(a)
print_all(b)
