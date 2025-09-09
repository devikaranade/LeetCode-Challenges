class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        freq = Counter()
        max_count = 0
        while right<len(s):
            c = s[right]
            freq[c]+=1
            while freq[c]>1:
                c_left = s[left]
                freq[c_left]-=1
                left+=1
            max_count=max(max_count, right-left+1)
            right+=1
        return max_count