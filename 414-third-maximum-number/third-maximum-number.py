class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count=1
        el = nums[0]
        for i in range(len(nums)):
            if nums[i]!=el:
                count+=1
                el = nums[i]
            if count==3:
                return nums[i]
        return nums[0]