class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = Queue()
q.push(7)
q.push(3)
q.push(31)
print(q.pop(), q.pop())
q.push(2)
q.push(22)
print(q.pop(), q.pop())
print(q.pop(), q.pop())