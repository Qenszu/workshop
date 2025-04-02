from zad2testy import runtests

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def SortH(p, k):
    if not p or not p.next or k == 0:
        return p
    
    dummy = Node(0)
    dummy.next = p
    last_sorted = p
    current = p.next
    
    while current:
        if current.val >= last_sorted.val:
            last_sorted = current
            current = current.next
        else:
            prev = dummy
            for _ in range(k):
                if prev.next == last_sorted:
                    break
                prev = prev.next
            
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            last_sorted.next = current.next
            current.next = prev.next
            prev.next = current
            current = last_sorted.next
    
    return dummy.next

runtests(SortH)