from list import *

def delete_or_insert(head, val):
    if head.val == val:
        return head.next
    p = head 
    while p.next is not None:
        if p.next.val == val:
            p.next = p.next.next
            return head
        p = p.next
    x = Node(val)
    p.next = x
    return head

a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9, 10, 13, 12])
b = delete_or_insert(a, 78)
print_all(b)
