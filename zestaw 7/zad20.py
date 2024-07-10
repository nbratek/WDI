from list import * 

def przedzialy(head):
    p = head
    prev = None
    while p is not None:
        flag = False
        a = p.next
        while a is not None:
            if a.val[0] <= p.val[1] <= a.val[1] or a.val[0] <= p.val[0] <= a.val[1]:
                if prev is not None:
                    prev.next = p.next
                else: 
                    head = p.next
                flaga = True
                break
            a = a.next
        if flaga is False:
            prev = p
        p = p.next
        
