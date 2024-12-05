class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def push(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.len += 1

    def pop(self):
        if self.empty():
            return "Queue is empty"
        val = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.len -= 1
        return val

    def front(self):
        if self.empty():
            return "Queue is empty"
        return self.head.val

    def size(self):
        return self.len

    def empty(self):
        return not self.head