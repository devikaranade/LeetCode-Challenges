class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        # empty stack condition
        if not self.stack:
            self.stack.append((val,val))
            return
        cur_min = self.stack[-1][1]
        self.stack.append((val, min(val,cur_min)))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()