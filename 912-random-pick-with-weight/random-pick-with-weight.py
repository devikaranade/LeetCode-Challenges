class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        for weight in w:
            prefix_sum+=weight
            self.prefix.append(prefix_sum)

    def pickIndex(self) -> int:
        target = self.prefix[-1]*random.random()
        low = 0
        high = len(self.prefix)
        while low<high:
            mid = low + (high-low)//2
            if target>self.prefix[mid]:
                low = mid+1
            else:
                high=mid
        return low
            

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()