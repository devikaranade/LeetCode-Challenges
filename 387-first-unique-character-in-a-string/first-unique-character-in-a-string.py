class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = Counter(s)
        for i in range(len(s)):
            if h[s[i]]<2:
                return i
        return -1