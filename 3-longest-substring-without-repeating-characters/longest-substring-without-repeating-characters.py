class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()
        start = end = res = 0
        while end<len(s):
            char = s[end]
            chars[char]+=1
            while chars[char]>1:
                char_left = s[start]
                chars[char_left]-=1
                start+=1
            res = max(res, end-start+1)
            end+=1
        return res
