class StringIterator:

    def __init__(self, compressedString: str):
        self.s = deque(compressedString)

    def next(self) -> str:
        while self.s:
            k = self.s.popleft()
            n = ""
            while self.s and self.s[0].isdigit():
                n+=self.s.popleft()
            n = int(n)
            if n!=1:
                self.s.appendleft(str(n-1))
                self.s.appendleft(k)
            return k
        else:
            return " "

    def hasNext(self) -> bool:
        return len(self.s)>1
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()