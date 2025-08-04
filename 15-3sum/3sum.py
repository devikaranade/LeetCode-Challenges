class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            self.twoSumII(nums, i, res)
        return res
    
    def twoSumII(self,nums, i, res):
        low = i+1
        high = len(nums)-1
        while low<high:
            total = nums[i]+nums[low]+nums[high]
            if total<0:
                low+=1
            elif total>0:
                high-=1
            else:
                res.append([nums[i],nums[low],nums[high]])
                while low<high and nums[low]==nums[low+1]:
                    low+=1
                while low<high and nums[high]==nums[high-1]:
                    high-=1
                low+=1
                high-=1
        return res
