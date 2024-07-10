from list import *

def piatki(n):
    l_piatek = 0 
    while n > 0:
        if n % 8 == 5:
            l_piatek += 1
            n //= 8
        else:
            n //= 8
    if l_piatek % 2 == 0:
        return True
    return False

def przeniesienie(head, val):
    x = Node(val)
    x.next = head
    head = x
    return head

def delete(head):
    p = head
    while p.next is not None:
        if piatki(p.next.val) is True:
            head = przeniesienie(head, p.next.val)
            p.next = p.next.next
        else:
            p = p.next
    return head

a = create_from_list([3, 6, 1, 4, 7, 2, 5, 9, 10, 13, 12])
b = delete(a)
print_all(b)
