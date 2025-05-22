class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = Counter()
        left = right = res = 0
        while right<len(s):
            r = s[right]
            d[r]+=1
            while d[r]>1:
                l=s[left]
                d[l]-=1
                left+=1
            res = max(res, right-left+1)
            right+=1
        return res 