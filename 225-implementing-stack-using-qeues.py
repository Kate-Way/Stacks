class MyStack:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def top(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]

    def empty(self) -> bool:
        if len(self.queue) > 0:
            return False
        return True




