class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        d = {0:1}
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum-k) in d:
                count+=d[curr_sum-k]
            d[curr_sum]=d.get(curr_sum,0)+1
        return count
