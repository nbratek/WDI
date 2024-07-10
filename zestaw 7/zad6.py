from list import *

def insert(head, val):
    p = head
    x = Node(val)
    while p.next is not None:
        p = p.next
    p.next = x
    return head

a = create_from_list([1, 3, 6, 13, 14, 18])
b = insert(a, 8)
print_all(b)