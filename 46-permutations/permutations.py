class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def rec(ans):
            if len(ans)==len(nums):
                final.append(ans[:])
                return 
            for num in nums:
                if num not in ans:
                    ans.append(num)
                    rec(ans)
                    ans.pop()

        final = []
        rec([])
        return final