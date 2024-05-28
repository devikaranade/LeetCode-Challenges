class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [-1, -100, 3, 99]
        def rev(left, right):
            while left<=right:
                nums[left], nums[right]=nums[right], nums[left]
                left+=1
                right-=1
        n = len(nums)
        k=k%n # k = 3
        rev(0, n-1) # [7,6,5,4,3,2,1]
        rev(0, k-1) # [5,6,7,4,3,2,1]
        rev(k, n-1) # [5,6,7,1,2,3,4]
