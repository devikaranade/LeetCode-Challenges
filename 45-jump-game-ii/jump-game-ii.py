class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        steps = 0
        s,e = 0, 0
        for i in range(n-1):
            e = max(e, i+nums[i])

            if i==s:
                steps+=1
                s=e
        return steps
        