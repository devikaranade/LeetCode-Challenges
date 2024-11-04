class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0])+ "/"+str(nums[1])
        ans = ""
        ans+=str(nums[0]) + "/("
        for i in range(1, len(nums)-1):
            ans+=str(nums[i])+'/'
        ans+=str(nums[-1])+')'
        return ans


          