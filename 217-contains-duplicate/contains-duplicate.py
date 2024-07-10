class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = Counter(nums)
        for v in h.values():
            if v>1:
                return True
        return False
        