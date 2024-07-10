from list import * 

def podlista(p):
    max_dl = 1
    dl = 0 
    v = p
    do_usuniecia = False
    if p is None:
        return None 
    if p.next is None:
        return None 
    while v.next is not None:
        if v.val < v.next.val:
            dl += 1
        else:
            dl = 1
        v = v.next
        if dl > max_dl:
            max_dl = dl
            do_usuniecia = True
        elif dl == max_dl:
            do_usuniecia = False
        if not do_usuniecia:
            return p
    s = Node(0)
    s.next = p 
    prev = s
    v = p 
    while v is not None:
        w = v 
        dl = 1
        while w.val < w.next.val:
            dl += 1
            w = w.next
        if dl == max_dl:
            prev.next = w.next
            return p
        v = w.next


a = create_from_list([1, 5, 6, 7, 8, 9, 2, 3, 1, 2, 6, 3, 2])
b = podlista(a)
print_all(b)