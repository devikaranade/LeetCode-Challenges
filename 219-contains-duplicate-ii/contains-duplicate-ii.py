class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]]=i
            else:
                diff = abs(i - h[nums[i]])
                if diff<=k:
                    return True
                h[nums[i]]=i
        return False
