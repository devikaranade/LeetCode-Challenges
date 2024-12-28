class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total, count = 0, 0
        d = {0:1}
        for i in nums:
            total+=i
            if total-k in d:
                count+=d[total-k]
            d[total]=1+d.get(total,0)
        return count


