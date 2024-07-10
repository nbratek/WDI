from list import * 

def delete(head):
    p = head
    while p.next is not None and p.next.next is not None:
        p.next = p.next.next
        p = p.next
    if p.next is not None:
        p.next = None


    return head


a = create_from_list([1, 3, 6, 13, 14, 18, 67, 34, 89, 65, 87, 36, 45])
b = delete(a)
print_all(b)