from list import *
class SparseArray:
    def __init__(self, default):
        self.head = None
        self.default = default
    
def init(default):
    return SparseArray(default)

def get(array, idx):
    v = array.head
    while v is not None:
        if v.idx == idx:
            return v.val
        v = v.next
    return array.default

def set(array, idx, val):
    v = array.head
    while v is not None: 
        if v.idx == idx:
            v. val = val
        v = v.next
    x = Node(idx, val)
    x.next = array.head
    array.head = x
