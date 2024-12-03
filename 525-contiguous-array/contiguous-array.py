class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1


        ans = 0
        sum = 0
        map_count = {}

        for i in range(len(nums)):
            sum+=nums[i]
            if sum==0:
                ans = i+1
            if sum in map_count:
                length = i-map_count[sum]
                ans = max(ans, length)
            else:
                map_count[sum]=i
        return ans
            
        

            
