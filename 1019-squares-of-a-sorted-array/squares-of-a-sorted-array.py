class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        n = len(nums)
        res = [0]*n
        for i in range(n-1, -1, -1):
            if abs(nums[l])<abs(nums[r]):
                sq = abs(nums[r])
                r-=1
            else:
                sq = abs(nums[l])
                l+=1
            res[i]=sq*sq
        return res