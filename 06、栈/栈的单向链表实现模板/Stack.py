class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.len = 0

    def push(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.len += 1

    def pop(self):
        if self.empty():
            return "Stack is empty"
        val = self.head.val
        self.head = self.head.next
        self.len -= 1
        return val

    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.head.val

    def size(self):
        return self.len
	
    def empty(self):
        return self.len == 0

stk = Stack()

stk.push(1)
stk.push(2)
stk.push(6)
stk.push(5)

while not stk.empty():
	print(stk.top())
	stk.pop()