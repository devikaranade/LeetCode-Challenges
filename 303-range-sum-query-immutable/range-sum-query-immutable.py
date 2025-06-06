class NumArray:

    def __init__(self, nums: List[int]):
        self.p = [nums[0]]
        for i in range(1, len(nums)):
            self.p.append(nums[i]+self.p[i-1])

    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return self.p[right]
        else:
            return self.p[right]-self.p[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)