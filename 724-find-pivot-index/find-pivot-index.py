class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        total = sum(nums)
        for i in range(len(nums)):
            sumRight = total - sumLeft - nums[i]
            if sumRight == sumLeft:
                return i
            sumLeft+=nums[i]
        return -1


