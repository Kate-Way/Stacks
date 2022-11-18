class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, val):
        new_element = Node(val)
        new_element.next = self.head
        self.head = new_element

    def peek(self):
        if self.head == None:
            return
        return self.head.val

    def pop(self):
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
# my_stack = Stack()
# my_stack.pop()
# print(my_stack.peek())
# my_stack.print()
# my_stack.push('google')
# my_stack.push('youtube')
# my_stack.push('linkedin')
# my_stack.print()
# print(my_stack.peek())
# my_stack.pop()
# my_stack.print()


# the logic is inverted when implementing with array to keep performance at O(1)

new_stack = []
new_stack.append('google')
new_stack.append('youtube')
new_stack.append('linkedin')
print(new_stack)
print(new_stack[-1])
new_stack.pop(-1)
print(new_stack)






