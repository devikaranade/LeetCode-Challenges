class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        word = ""
        for s in strs:
            if len(s)<min_length:
                min_length = len(s)
                word = s
        i = 0
        while i<min_length:
            for s in strs:
                if s[i]!=word[i]:
                    return s[:i]
            i+=1
        return word[:min_length]