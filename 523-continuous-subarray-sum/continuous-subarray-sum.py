class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod = 0
        d = {0:-1}
        for i in range(len(nums)):
            mod = (mod + nums[i])%k
            if mod not in d:
                d[mod]=i
            else:
                if i-d[mod]>1:
                    return True
        return False
