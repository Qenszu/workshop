class new:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0
    
    def display(self):
        print(self.data)
    
    def add_element(self, val):
        if self.is_empty():
            self.data.append(val)
        else:
            self.data.append(val)
            self.heapsort()

    def heapify(self, n, i):
        maxi = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and self.data[left] > self.data[maxi]:
            maxi = left
        if right < n and self.data[right] > self.data[maxi]:
            maxi = right

        if maxi != i:
            self.data[i], self.data[maxi] = self.data[maxi], self.data[i]
            self.heapify(n, maxi)




A = new()
new.add_element(A, 5)
new.display(A)
new.add_element(A, 4)
new.display(A)
