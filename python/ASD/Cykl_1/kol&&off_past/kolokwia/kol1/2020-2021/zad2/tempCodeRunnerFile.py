from zad2testy import runtests

class Node:
  def __init__(self, val):
    self.val = val    
    self.next = None 

def swap(p, node1, node2):  
   sentinel = Node(None)
   sentinel.next = p
      
   back1 = sentinel
   back2 = sentinel 

   while back1.next != node1:
      back1 = back1.next
  
   while back2.next != node2:
      back2 = back2.next

   if node1.next == node2:
      node1.next = node2.next
      node2.next = node1
      back1.next = node2

      return sentinel.next

   back1.next = node1.next
   back2.next = node2.next

   node1.next = back2.next
   back2.next = node1

   node2.next = back1.next
   back1.next = node2

   return sentinel.next

def display(p):
    current = p
    while current is not None:
        print(current.val, end="")
        if current.next is not None:
            print(" --> ", end="")
        current = current.next
    print()  # For a new line at the end
    

def middle(node1, node2):
   tmp1 = node1
   cnt = 0

   while tmp1 != node2:
      tmp1 = tmp1.next
      cnt +=1

   tmp1 = node1

   for i in range(cnt//2):
      tmp1 = tmp1.next

   return tmp1

p = Node(4)
p.next = Node(3)
p.next.next = Node(2)
p.next.next.next = Node(1)
q = p.next.next.next


def mergesort(p, node1, node2):
   #tail = node2.next
   #node2.next = None
   if node1 !=  node2:
      k = middle(node1, node2)
      mergesort(p, node1, k)
      if k.next != None:
         mergesort(p, k.next, node2)
      k.next = None

      if node1 != None and node2 != None:
         if node1.val < node2.val:
            result = node1
            node1 = node1.next
         else:
            result = node2
            node2 = node2.next

      p = result

      while node1 != None and node2 != None:
        if node1.val < node2.val:
          p.next = node1
          p = p.next
          node1 = node1.next
        else:
           p.next = node2
           p = p.next
           node2 = node2.next
      
      if node1 != None:
         p.next = node1
      else:
         p.next = node2

      p.next = tail
      return result

display(p)
p = mergesort(p, p, p.next)
display(p)


def SortH(p,k):
    # tu prosze wpisac wlasna implementacje
    pass


#runtests( SortH ) 