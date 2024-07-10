from list import *

def delete(head):
    p = head
    while p.next is not None:
        v1 = p.next.val
        v2 = p.val
        if v1 % v2 == 0:
            p.next = p.next.next
        else: 
            p = p.next
    return head 

a = create_from_list([3, 6, 7, 21, 44, 2, 4, 8, 11])
b = delete(a)
print_all(b)