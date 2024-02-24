class MyStack:

    def __init__(self):
        self.s1 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        key = self.s1.pop(-1)
        return key
        

    def top(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        if not self.s1:
            return True
        return False

        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()