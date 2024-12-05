class Stack:
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        if self.empty():
            return "Stack is empty"
        return self.data.pop()

    def top(self):
        if self.empty():
            return "Stack is empty"
        return self.data[-1]

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

stk = Stack()

stk.push(1)
stk.push(2)
stk.push(6)
stk.push(5)

while not stk.empty():
	print(stk.top())
	stk.pop()