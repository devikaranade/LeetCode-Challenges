class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            total = max(nums[i], nums[i]+total)
            max_sum = max(total, max_sum)
        return max_sum
        