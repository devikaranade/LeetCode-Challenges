class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums)-1
        if len(nums)==1:
            return True
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i]>=last:
                last = i
        return last==0
            

        
        
        # while i<=len(nums)-1:
        #     if nums[i]>steps:
        #         steps=nums[i] #steps = 0->2 -> 3 -> 4
        #     steps = steps-1  # i = 2 -> 3
        #     if steps<0:
        #         return False
        #     i+=1
        # return True


            
                
        