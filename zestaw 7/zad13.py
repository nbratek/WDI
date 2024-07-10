from list import *

def delete(head):
    p = head 
    q = p.next
    while q.next is not None:
        if p.val > q.val:
            p.next = q.next
            p = p.next
            q = p.next
        else:
            p = p.next
            q = p.next
    if q is not None and p.val > q.val:
        p.next = None
        p = p.next
    elif q is not None and p.val <= q.val:
        p = p.next
        q = p.next
    return head

a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9, 10, 13, 12])
b = delete(a)
print_all(b)