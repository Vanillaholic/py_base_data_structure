class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0

    def push(self, val):
        self.data.append(val)
        self.tail += 1

    def pop(self):
        if self.empty():
            return "Queue is empty"
        val = self.data[self.head]
        self.head += 1
        return val

    def front(self):
        if self.empty():
            return "Queue is empty"
        return self.data[self.head]

    def size(self):
        return self.tail - self.head

    def empty(self):
        return self.head == self.tail

q = Queue()

q.push(1)
q.push(2)
q.push(6)
q.push(5)

while not q.empty():
	print(q.front())
	q.pop()
