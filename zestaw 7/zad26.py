from list import * 

def czy_zawiera(head1, head2):
    p = head1
    q = head2
    while head1 is not None:
        if head2 is None:
            return True
        if head1.val != head2.val:
            p = p.next
            head1 = p
            head2 = q
        else:
            head1 = head1.next
            head2 = head2.next
    if head1 is None and head2 is None:
        return True
    return False


def check(p, q):
    r1 = p
    r2 = q
    if czy_zawiera(r1, r2) or czy_zawiera(r2, r1):
        return True
    return False
