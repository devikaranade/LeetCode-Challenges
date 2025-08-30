class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        char_count = {}
        max_len = 0
        for end, char in enumerate(s):
            char_count[char]=char_count.get(char, 0)+1
            while len(char_count)>2:
                char_count[s[start]]-=1
                if char_count[s[start]]==0:
                    del char_count[s[start]]
                start+=1
            max_len = max(max_len, end-start+1)
        return max_len