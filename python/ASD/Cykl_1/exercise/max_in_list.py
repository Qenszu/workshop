class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def find_max(first):
    p = first.next
    maxi = first.data
    while p.next != None:
        if p.data > maxi:
            maxi = p.data
        p = p.next
    return maxi

first = Node(1)
first.next = Node(2)
first.next.next = Node(10)
first.next.next.next = Node(4)

print(find_max(first))