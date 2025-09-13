class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1, 1
        n = len(nums)
        left_product = [1]*n
        right_product = [1]*n

        for i in range(1, n):
            left = left*nums[i-1]
            left_product[i]=left
        
        for i in range(n-2, -1, -1):
            right = right*nums[i+1]
            right_product[i]=right
        
        res = [1]*n
        for i in range(n):
            res[i]=left_product[i]*right_product[i]
        return res

