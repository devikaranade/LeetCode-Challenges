class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        h = {}
        for i, num in enumerate(s):
            if num not in h:
                h[num]=i
        
        res = []
        for i in nums:
            res.append(h[i])
        return res