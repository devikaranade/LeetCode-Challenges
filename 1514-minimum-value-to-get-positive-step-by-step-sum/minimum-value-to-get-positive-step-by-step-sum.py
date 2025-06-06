class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0
        for num in nums:
            total+=num
            min_val = min(min_val, total)
        return -min_val+1
        # m = 100
        # n = len(nums)

        # left = 1
        # right = m*n+1
        # while left<right:
        #     mid = (left+right)//2
        #     total = mid
        #     is_valid =True
        
        #     for num in nums:
        #         total+=num
        #         if total<1:
        #             is_valid=False
        #             break
        #     if is_valid:
        #         right=mid
        #     else:
        #         left=mid+1
        # return left
        