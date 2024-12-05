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

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push( self.s1.pop() )
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2.empty():
            while not self.s1.empty():
                self.s2.push( self.s1.pop() )
        return self.s2.top()

    def empty(self) -> bool:
        return self.s1.empty() and self.s2.empty()


q = MyQueue()

q.push(1)
q.push(2)
q.push(6)
q.push(5)


while not q.empty():
    print(q.peek())
    q.pop()