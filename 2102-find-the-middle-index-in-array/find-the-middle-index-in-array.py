class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        left = 0
        for i in range(len(nums)):
            rsum = s-left-nums[i] 
            if rsum==left:
                return i
            left+=nums[i]
        return -1



        
