class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

def print_all(p):
    if p is not None:
        print(p.val, end = ' ')
        print_all(p.next)
    else:
        print()

def list_all(p):
    if p is not None:
        return [p.val] + list_all(p.next)
    else:
        return []

def create_from_list(L):
    g = Node(None)
    p = g
    for el in L:
        p.next = Node(el)
        p = p.next
    return g.next