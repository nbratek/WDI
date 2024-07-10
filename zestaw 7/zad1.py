from list import *
def is_element(p, val):
    while p is not None:
        if p.val == val:
            return True
        p = p.next
    return False

def insert1(head, val):
    x = Node(val)
    x.next = head 
    return x

def insert2(head, val):
    p = head
    x = Node(val)
    while p.next is not None:
        p = p.next
    p.next = x
    return head

def delete1(head, val):
    if head is None:
        return None
    return head.next

def delete2(head, val):
    if head.val == val:
        return head.next
    v = head 
    while v is not None:
        if v.next is not None and v.next.val == val:
            v.next = v.next.next
        v = v.next
    return head

def delete3(head, val):
    s = Node(0)
    s.next = head
    v = s
    while v is not None:
        if v.next is not None and v.next.val == val:
            v.next = v.next.next
        else:
            v = v.next
    return s.next

a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9, 10, 13, 12])
b = delete2(a, 7)
print_all(b)