from list import *

def roznica(s1, s2):
    for i in range(min(s1, s2)):
        if s1[i] != s2[i]:
            return i 
    if len(s1) == len(s2):
        return -1
    return min(len(s1), len(s2))

def napis(head, s):
    p = head
    while p.next is not None:
        r = roznica(s, p.next.val)
        if r == -1:
            return False
        if r == len(p.next.val):
            p = p.next
            continue
        if r == len(s) or ord(s[r]) < ord(p.next.val[r]):
            x = Node(s)
            x.next = p.next
            p.next = x
            return
        
        p = p.next

    if p.val == s:
        return 
    p.next = Node(s)
    
        