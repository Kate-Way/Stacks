class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(len(self.stack)-1)

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
