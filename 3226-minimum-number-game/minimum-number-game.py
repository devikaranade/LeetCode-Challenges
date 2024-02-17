class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []
        while len(nums):
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            res.append(bob)
            res.append(alice)
        return res
