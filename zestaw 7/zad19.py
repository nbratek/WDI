from list import *

def delete(head):
    p = head
    while p.next is not None:
        if p.val == p.next.val:
            q = p.next
            while q is not None and p.val == q.val:
                q = q.next
            p.next = q
        else:
            p = p.next
    return head 


a = create_from_list([3, 6, 1, 4, 7, 7, 7, 7, 2, 5, 9, 10, 13, 12])
b = delete(a)
print_all(b)

        