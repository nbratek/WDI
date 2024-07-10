from list import *

def reverse(head):
    p = None
    q = head.next
    while head is not None:
        head.next = p 
        p = head
        head = q
        if q.next is not None:
            q = q.next
    return p

def add(head):
    r = reverse(head)
    p = r
    while p is not None: 
        if p.val < 9:
            p.val += 1
            z = reverse(r)
            return z 
        if p.val == 9:
            p.val = 0
            p = p.next
    if p is None: 
        a = reverse(r)
        x = Node(1)
        x.next = a
        a = x
        return a


a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9])
b = add(a)
print_all(b)