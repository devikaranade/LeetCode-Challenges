class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.total = 0
        
        

    def next(self, val: int) -> float:
        '''
        window = [1, 11, 3]
        total = 0+1 = 1+ 10 = 11+3 = 14
        return 1/1 = 1.0 = 14/3 = 4.666

        '''
        
        if len(self.window)>=self.size: 
            self.total-=self.window.popleft()
        self.total += val
        self.window.append(val)
        return self.total/len(self.window)
    

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)