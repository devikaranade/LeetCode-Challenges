class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        word = strs[0]
        for i in range(len(word)):
            for w in strs[1:]:
                if i == len(w) or w[i]!=word[i]:
                    return word[0:i]
        return word
        