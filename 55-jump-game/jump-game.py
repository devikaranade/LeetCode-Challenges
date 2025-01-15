class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        if len(nums)==1:
            return True
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i]>=last:
                last =  i 
        return last==0
