class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.maxNumbers = maxNumbers
        self.q = deque(range(self.maxNumbers))
        self.visited = [True]*self.maxNumbers

    def get(self) -> int:
        if not self.q:
            return -1
        slot = self.q.popleft()
        self.visited[slot]=False
        return slot

    def check(self, number: int) -> bool:
        return self.visited[number]

    def release(self, number: int) -> None:
        if self.visited[number]:
            return
        self.q.append(number)
        self.visited[number]=True

      
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)