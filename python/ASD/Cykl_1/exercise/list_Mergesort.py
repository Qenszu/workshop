from time import sleep

class Node:
    def __init__(self, value):
        self.next = None
        self.val = value

def display(node):
    while node != None:
        print(node.val, end = " --> ")
        node = node.next
        sleep(0.2)
    print("None")

def append(node, data):
    while node.next != None:
        node = node.next
    new_node = Node(data)
    node.next = new_node

def split(head):
    res = head
    if head is None:
        return None
    if head.next is None:
        return None
    if head.next.next is None:
        return head.next
    while head.next and head.next.next:
        head = head.next.next
        res = res.next
    return res.next

def list_merge_sort(headh):
    head = headh.next
    if head is None or head.next is None:
        return
    right = Node(None)
    right.next = split(head)
    left = Node(None)
    left.next = head
    tmp = head
    if head.next == right.next:
        left.next = head
        left.next.next = None
    else:
        while tmp.next != right.next:
            tmp = tmp.next
        tmp.next = None
    
    list_merge_sort(left)
    list_merge_sort(right)

    if left.next != None and right.next != None:    
        if left.next.val < right.next.val:
            headh.next = left.next
            left = left.next.next
            right = right.next
        else:
            headh.next = right.next
            right = right.next.next
            left = left.next
            
        head = headh.next
        head.next = None

    while left != None and right != None:
        if left.val < right.val and left != head:
            head.next = left
            left = left.next
        else:
            if head != right:
                head.next = right
                right = right.next
        head = head.next
   
    if left != None:
        head.next = left
    else:
        head.next = right
    

def sort_list(p):
    new_node = p
    p = Node(None)
    p.next = new_node
    list_merge_sort(p)
    return p.next

p = Node(6)
append(p, 5)
append(p, 4)
append(p, 3)
append(p, 2)
append(p, 6)
append(p, 8)
append(p, 1)
append(p, 19)
append(p, 3)
append(p, 10)
append(p, 5)
print("Input list: ", end = "")
display(p)
p = sort_list(p)
print("Sorted list: ", end = "")
display(p)




