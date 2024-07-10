from list import *

def delete(head):
    p = head
    while p.next.next is not None:
        p = p.next
    p.next = p.next.next
    return head


a = create_from_list([1, 3, 6, 13, 14, 18])
b = delete(a)
print_all(b)

