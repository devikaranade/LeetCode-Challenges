class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, final, comb):
            if len(comb)==len(nums):
                final.append(comb.copy())
                return
            for i in nums:
                if i not in comb:
                    comb.append(i)
                    backtrack(nums, final, comb)
                    comb.pop()
            
        res = []
        backtrack(nums, res, [])
        return res