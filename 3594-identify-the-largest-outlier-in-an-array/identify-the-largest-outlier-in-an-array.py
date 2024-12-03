class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        total = sum(nums)
        res = -1001

        for i in nums:
            freq[i]+=1

        for i in nums:
            total-=i
            freq[i]-=1
            if not freq[i]:
                del freq[i]
            if total%2==0 and total//2 in freq:
                res = max(res, i)
            freq[i]+=1
            total+=i
        return res
