class MyQueue:

    def __init__(self):
        self.q1 = []
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        

    def pop(self) -> int:
        key = self.q1.pop(0)
        return key

        

    def peek(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        if not len(self.q1):
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()