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
        
class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.push(x)

    def pop(self) -> int:
        while self.q1.size() > 1:
            self.q2.push( self.q1.pop() )
        ret = self.q1.pop()
        while self.q2.size() > 0:
            self.q1.push( self.q2.pop() )
        return ret

    def top(self) -> int:
        while self.q1.size() > 1:
            self.q2.push( self.q1.pop() )
        ret = self.q1.pop()
        self.q2.push(ret)
        while self.q2.size() > 0:
            self.q1.push( self.q2.pop() )
        return ret

    def empty(self) -> bool:
        return self.q1.empty()
 
stk = MyStack()
stk.push(1)
stk.push(2)
stk.push(6)
stk.push(5)

while not stk.empty():
    print(stk.top())
    stk.pop()