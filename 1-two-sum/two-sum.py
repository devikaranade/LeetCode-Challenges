class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        # {2 - 0 , }
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in h:
                h[nums[i]]=i
            else:
                return [i, h[diff]]

            
        