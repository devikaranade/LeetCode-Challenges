class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        s = set(nums)

        for num in s:
            if num-1 not in s:
                curr = num
                streak = 1

                while curr+1 in s:
                    curr+=1
                    streak+=1
                
                max_streak = max(max_streak, streak)
        return max_streak