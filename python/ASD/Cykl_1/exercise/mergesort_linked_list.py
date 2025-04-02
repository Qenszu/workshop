class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        """Dodaje nowy element na koniec listy"""
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

    def print_list(self):
        """Wypisuje listę"""
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

def find_middle(head):
    """Znajduje środek listy za pomocą slow & fast pointer"""
    if not head or not head.next:
        return head
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    middle = slow.next
    slow.next = None  # Dzielimy listę na dwie części
    return middle

def merge_sorted_lists(left, right):
    """Scala dwie posortowane listy"""
    dummy = Node(0)  # Węzeł pomocniczy
    tail = dummy

    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right  # Dołącz pozostałe elementy
    return dummy.next

def merge_sort(head):
    """Sortuje listę odsyłaczową za pomocą Merge Sort"""
    if not head or not head.next:
        return head
    
    middle = find_middle(head)  # Znajdź środek
    left = merge_sort(head)     # Sortuj lewą połowę
    right = merge_sort(middle)  # Sortuj prawą połowę

    return merge_sorted_lists(left, right)  # Połącz obie części

# Przykład użycia
ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(1)
ll.append(3)

print("Przed sortowaniem:")
ll.print_list()

ll.head = merge_sort(ll.head)

print("Po sortowaniu:")
ll.print_list()
