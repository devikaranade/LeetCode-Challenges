class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        s = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]<target:
                    s.add((i,j))
        return len(s)

        