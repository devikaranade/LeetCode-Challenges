class ProductOfNumbers:

    def __init__(self):
        self.q = []
        self.prod = 1
        

    def add(self, num: int) -> None:
        if num:
            self.prod *= num
            self.q.append(self.prod)
        else:
            self.q = []
            self.prod = 1

        

    def getProduct(self, k: int) -> int:
        if len(self.q)<k:
            return 0
        elif len(self.q)==k:
            return self.prod
        else:
            return int(self.q[-1]/self.q[-1-k])
        




        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)