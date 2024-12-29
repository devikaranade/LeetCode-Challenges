class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        pre = 0
        res = 0
        for x in nums:
            if x==0:
                if s==pre:
                    res+=2
                elif s==pre+1 or s==pre-1:
                    res+=1
            s-=x
            pre+=x
        return res
