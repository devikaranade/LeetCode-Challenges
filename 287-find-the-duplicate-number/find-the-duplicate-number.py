class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        for k,v in c.items():
            if v>=2:
                return k