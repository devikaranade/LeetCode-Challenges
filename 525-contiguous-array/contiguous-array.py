class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map_0 = defaultdict(list)
        total = 0
        ans = 0
        map_0[0].append(-1) # {0: -1}
        for i, num in enumerate(nums):
            total+=1 * (1 if num else -1)
            if total in map_0:
                ans = max(ans, i-map_0[total][0])
            map_0[total].append(i)
        return ans
