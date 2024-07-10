from list import *

def merge(p, q):
    if p is None:
        return q
    if q is None:
        return p
    if p.val < q.val:
        head = merge(p.next, q)
        p.next = head
        return p
    else:
        head = merge(p, q.next)
        q.next = head
        return q

def reverse(head):
    p = None
    while head is not None:
        tmp = head
        head = tmp.next
        tmp.next = p
        p = tmp
    return p    

def merge_i(p, q):
    head = None 
    while p is not None and q is not None:
        if q.val < p.val:
            tmp = q
            q = q.next
            tmp.next = head
            head = tmp
        else:
            tmp = p
            p = p.next
            tmp.next = head
            head = tmp
    if p is None:
        while q is not None:
            tmp = q
            q = q.next
            tmp.next = head
            head = tmp
    if q is None:
        while p is not None:
            tmp = p
            p = p.next
            tmp.next = head
            head = tmp
    return reverse(head)

a = create_from_list([1, 3, 5, 7, 9])
b = create_from_list([2, 6, 8])
c = merge(a, b)
print_all(c)
