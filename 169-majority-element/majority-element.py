class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict()
        key = len(nums)//2
        for i in nums:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for k,v in m.items():
            if v>key:
                return k
     