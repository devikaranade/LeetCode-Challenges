class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = Counter(nums)
        for k,v in h.items():
            if v>1:
                return True
        return False
