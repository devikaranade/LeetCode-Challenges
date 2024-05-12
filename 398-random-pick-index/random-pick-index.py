class Solution:

    def __init__(self, nums: List[int]):
        self.index={}
        for i, num in enumerate(nums):
            if num not in self.index:
                self.index[num]=[]
            self.index[num].append(i)
        

    def pick(self, target: int) -> int:
        k = self.index[target]
        return random.choice(k)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)