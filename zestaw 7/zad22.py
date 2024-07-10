from list import * 

def cykl(p):
    if p is None: 
        return False
    if p.next is None:
        return False
    fast = p
    slow = p 
    while fast.next is not None and fast.next.next is not None: 
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

