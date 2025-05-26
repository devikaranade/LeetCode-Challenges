class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = Counter(s)
        t_map = Counter(t)
        return t_map==s_map