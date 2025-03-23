""""
Będziemy korzystać z kilku wskaźników pomocniczych.
       1. Pierwszy wskaźnik wskazuje na ostatni posortowany element tablicy
       2. drugi wskaźnik wskazuje na pierwszy nieposortwany element tablicy
W kazdej iteracji wśród nieposortowanych węzłów szukamy węzła o największej wartości. 
Zwracamy wskaźnik na niego i coś tam jeszcze
Następnie wypinamy ten element z listy i 
Iteracje kontynuujemy az opala sie zamknie
Skoro insert wstawail w odpowiednie miejsce to w ostatniej iteracji pierwszy wskaznik 
bedzie wskazyl na liste ktora jest posortowana
"""

# 2 --> 3 --> 5 --> 4 --> 8 --> 6 --> None

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

def append(first, value):
    node = first
    new_node = Node(value)
    if first is None:
        return new_node
    while node.next != None:
        node = node.next
    node.next = new_node

    return first

def display(first):
    node = first
    print(node.data, end = " --> ")
    while node.next != None:
        node = node.next
        print(node.data, end = " --> ")
    print("None")

def my_sort(p):
    start = p
    head = p
    tail = Node(None)
    tail.next = head

    while head.next != None:
        if head.next.data < head.data:
            tmp = head.next
            head.next = head.next.next
            while start.next.data < tmp.data:
                start = start.next
            tmp.next = start.next
            start.next = tmp
            start = p 
        else:
            head = head.next
            tail = tail.next 

def find_min(p):
    mini = float("inf")
    result = p
    while p.next != None:
        x = p.data
        if x < mini:
            result = p
            mini = x
        p = p.next
    return result

def put_on_start(p, q):
    head = p

    if head != q:
        while head.next != q:
            head = head.next

        head.next = q.next
        q.next = p 
    return q

def selection_sort(p):
    head = p
    sorted_head = Node(None)
    sorted_head.next = p
    tail = sorted_head
    p = sorted_head

    while sorted_head.next != None:
        if sorted_head.data == sorted_head.next.data:
            sorted_head = sorted_head.next
        else: 
            mini = find_min(sorted_head.next)
            sorted_head.next = put_on_start(sorted_head.next, mini)
            sorted_head = sorted_head.next
    
    while sorted_head.data > head.data:
        head = head.next
        tail = tail.next
    tail = tail.next
    tail.next = put_on_start(tail.next, sorted_head)

    return p.next


p = Node(4)
append(p, 3)
append(p, 5)
append(p, 4)
append(p, 8)
append(p, 6)
append(p, 15)
append(p, 9)
append(p, 6)
append(p, 7)

display(p)

p = selection_sort(p)

display(p)




        

