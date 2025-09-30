class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        freq = defaultdict(int)
        max_count=0
        while r<len(s):
            ch = s[r]
            freq[ch]+=1
            while freq[ch]>1:
                ch_l = s[l]
                freq[ch_l]-=1
                l+=1
            max_count = max(max_count, r-l+1)
            r+=1
        return max_count
                