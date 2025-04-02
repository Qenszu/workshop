class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


def add(first, val):
    new = Node(val)

    if first.data > val:
        new.next = first
        return new


    p = first.next
    tail = first

    while p != None:
        if p.data > val:
            new.next = p
            tail.next = new
            return first
        p = p.next
        tail = tail.next
    
    tail.next = new
    return first

    

first = Node(2)
first.next = Node(2)
first.next.next = Node(3)
first.next.next.next = Node(5)
#first.next.next.next.next = Node(6)

first = add(first, 2)

def display(first):
    node = first
    print(node.data, end = " --> ")
    while node.next != None:
        node = node.next
        print(node.data, end = " --> ")
    print("None")

display(first)
