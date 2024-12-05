#!/usr/bin/python
# Write Python 3 code in this online editor and run it.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
	
    def size(self):
        return self.len

    def insert(self, pos, val):
        if pos < 0 or pos > self.len:
            raise ValueError("无效的位置")
        newNode = ListNode(val)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            prev = self.head
            for _ in range(pos - 1):
                prev = prev.next
            newNode.next = prev.next
            prev.next = newNode
        self.len += 1

    def delete(self, pos):
        if pos < 0 or pos >= self.len:
            raise ValueError("无效的位置")
        if pos == 0:
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(pos - 1):
                prev = prev.next
            prev.next = prev.next.next
        self.len -= 1

    def update(self, pos, val):
        if pos < 0 or pos >= self.len:
            raise ValueError("无效的位置")
        if pos == 0:
            self.head.val = val
        else:
            current = self.head
            for _ in range(pos):
                current = current.next
            current.val = val

    def search(self, val):
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next
        return None

    def index(self, val):
        index = 0
        current = self.head
        while current:
            if current.val == val:
                return index
            index += 1
            current = current.next
        return -1
	
    def print(self):
        current = self.head
        while current:
            print(current.val, end='->')
            current = current.next
        print('None')

l = LinkedList()

l.insert(0, 9)
l.print()
l.insert(1, 5)
l.print()
l.insert(0, 8)
l.print()
l.insert(1, 2)
l.print()
l.insert(1, 3)
l.print()

l.delete(1)
l.print()
l.delete(0)
l.print()

l.update(2, 999)
l.print()
l.update(1, 666)
l.print()

node = l.search(666)
if node:
    print(node.val)
else:
    print(None)

x = l.index(999)
print(x)
x = l.index(333)
print(x)