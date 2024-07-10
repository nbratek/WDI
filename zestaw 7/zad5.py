class Node:
    def __init__(self, val):
        self.next = None
        self.val = val
        
def rozdzielanie(p):
    heads = [Node(i) for i in range(10)]
    tails = [heads(i) for i in range(10)]
    while p is not None:
        idx = p.val % 10
        tmp = p.next
        tails[idx].next = p
        p = tmp
    for i in range(9):
        tails[i].next = heads[i + 1].next
    return heads[0].next