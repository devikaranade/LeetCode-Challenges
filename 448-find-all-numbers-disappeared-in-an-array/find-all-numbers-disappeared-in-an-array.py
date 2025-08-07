class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = abs(nums[i-1])-1
            if nums[idx] > 0:
                nums[idx]*=-1
        
        for i in range(1,len(nums)+1):
            if nums[i-1]>0:
                res.append(i)
        return res













        # res = []
        # for i in range(len(nums)):
        #     new_index = abs(nums[i])-1
        #     if nums[new_index]>0:
        #         nums[new_index]*=-1
        
        # for i in range(1, len(nums)+1):
        #     if nums[i-1]>0:
        #         res.append(i)

        # return res

