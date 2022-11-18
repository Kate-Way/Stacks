
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        curr = Node(val)
        if self.head == None:
            self.head = curr
            self.tail = curr
            return
        self.tail.next = curr
        self.tail = curr

    def peek(self):
        if self.head == None:
            return
        return self.head.val

    def dequeue(self):
        if self.head == None:
            return
        curr = self.head
        self.head = curr.next


    def print(self):
        elems = []
        curr = self.head
        if curr == None:
            print(elems)
            return
        elems.append(curr.val)
        while curr.next:
            curr = curr.next
            elems.append(curr.val)
        print(elems)

# Test
# my_queue = Queue()
# my_queue.enqueue(23)
# my_queue.enqueue(50)
# my_queue.enqueue(67)
# my_queue.print()
# print(my_queue.peek())
# my_queue.dequeue()
# my_queue.print()


from collections import deque

new_queue = deque()
new_queue.append(3)
new_queue.append(5)
new_queue.append(7)
print(new_queue)
print(new_queue.popleft())
print(new_queue)

