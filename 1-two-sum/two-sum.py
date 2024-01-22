class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for k,v in enumerate(nums):
            diff = target - v
            if diff not in h:
                h[v] = k
            else:
                return h[diff],k